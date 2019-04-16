# Tools for use on the Jetson tegra TX2 Nvidia edge compute node (JTX2)

Specifically the AAEON form-factor.


## jtx2-show-gpu

![GPU Tracker](docs/pics/activity.png)


This tool displays the current GPU usage verifying that the GPU core and supporting libraries are actually in
use.

`$ jtx2-show-gpu --help`

```zsh

Usage: jtxt2-show-gpu [OPTIONS]

  Plot JTX2 GPU usage

Options:
  --version                 Show the version and exit.
  -i, --interval INTEGER    Update graph rate in ms  [default: 250]
  -f, --gpu-load-file TEXT  Load file  [default: /sys/devices/gpu.0/load]
  --help                    Show this message and exit.
```

# Install

Tools are packaged as typical setuptools packaged applications.

Clone repo and do `$ pip install . ` in virtualenv. Tool is available as
`jtx2-show-gpu` in path.



# Resources

 - https://github.com/jetsonhacks/gpuGraphTX

