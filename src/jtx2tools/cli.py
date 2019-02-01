import sys
import os
import click
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation
from collections import deque


@click.command(context_settings=dict(max_content_width=120))
@click.version_option()
@click.option(
    '-i',
    '--interval',
    default=250,
    help='Update graph rate in ms',
    show_default=True,
)
@click.option(
    '-f',
    '--gpu-load-file',
    default='/sys/devices/gpu.0/load',
    help='Load file',
    show_default=True,
)
def cli(interval, gpu_load_file):
    """
    Plot JTX2 GPU usage
    """

    # Subplot for the GPU activity
    gpuAx = plot.subplot2grid((1, 1), (0, 0), rowspan=2, colspan=1)
    # For the comparison
    gpuLine, = gpuAx.plot([], [])
    # The line points in x,y list form
    gpuy_list = deque([0] * 240)
    gpux_list = deque(np.linspace(60, 0, num=240))

    fill_lines = 0

    def initGraph():
        gpuAx.set_xlim(60, 0)
        gpuAx.set_ylim(-5, 105)
        gpuAx.set_title('GPU History')
        gpuAx.set_ylabel('GPU Usage (%)')
        gpuAx.set_xlabel('Seconds')
        gpuAx.grid(color='gray', linestyle='dotted', linewidth=1)

        gpuLine.set_data([], [])
        fill_lines = gpuAx.fill_between(gpuLine.get_xdata(), 50, 0)

        return [gpuLine] + [fill_lines]

    def updateGraph(frame):
        """Now draw the GPU usage"""

        gpuy_list.popleft()
        try:
            with open(gpu_load_file, 'r') as gpuFile:
                fileData = gpuFile.read()

                # The GPU load is stored as a percentage * 10, e.g 256 = 25.6%
                gpuy_list.append(int(fileData) / 10)
                gpuLine.set_data(gpux_list, gpuy_list)
                fill_lines.remove()
                fill_lines = gpuAx.fill_between(gpux_list, 0, gpuy_list, facecolor='cyan', alpha=0.50)

                return [gpuLine] + [fill_lines]
        except FileNotFoundError:
            click.echo(f'Error reading {gpu_load_file}')
            return []

    fig = plot.figure(figsize=(6, 2))
    animation = FuncAnimation(
        fig,
        updateGraph,
        frames=200,
        init_func=initGraph,
        interval=interval,
        blit=True,
    )

    plot.subplots_adjust(top=0.85, bottom=0.30)
    fig.set_facecolor('#F2F1F0')
    fig.canvas.set_window_title('GPU Activity Monitor')

    plot.show()
