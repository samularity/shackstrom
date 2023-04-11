shackstrom - proprietary interface to mqtt
==========================================


## What it does?

It's only possible to read the energy consumption data manually over the webinterface.

The script read the current (total) energy consumption from the webinterface once every minute.
The data is then parsed, transformed in Watthours and published it via mqtt.


## how to install

just add the following part to your nix-config (and update the rev&hash )

```
{ pkgs, ... }:
let
  src = pkgs.fetchFromGitHub {
    repo = "shackstrom";
    owner = "samularity";
    rev = "adfbdc7d12000fbc9fd9367c8ef0a53b7d0a9fad";
    hash = "sha256-77vSX2+1XXaBVgLka+tSEK/XYZASEk9iq+uEuO1aOUQ=";
  };
  pkg = pkgs.writers.writePython3 "test_python3" {
    libraries = [ pkgs.python3Packages.requests pkgs.python3Packages.paho-mqtt  ];
  } (builtins.readFile "${src}/shackstrom.py");
in
{
    systemd.services = {
      u300-power = {
        enable = true;
        environment = { 
          DATA_URL = "http://10.42.20.255/csv.html";
          BROKER = "mqtt.shack";
        };
        serviceConfig = {
          Restart = "always";
          ExecStart = pkg;
          RestartSec = "15s";
        };
        wantedBy = [ "multi-user.target" ];
      };
    };
}
```

## Device Info

User-Manual: https://www.sms-guard.org/downloads/IPswitch-S0-mini-Anleitung.pdf

![GIF](IPs-S0-mini-2.gif) 
