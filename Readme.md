shackstrom - proprietary interface to mqtt
==========================================


## What it does?

It's only possible to read the energy consumption data manually over the webinterface.

The script read the current (total) energy consumption from the webinterface once every minute.
The data is then parsed, transformed in Watthours and published it via mqtt.


## how to install

just add the following part to your nix-config

```
{ pkgs }:
{
    systemd.services.shackstrom={
        script=pkgs.callPackage ./default.nix {};
        enable = True;
    }
}
```

## Device Info

User-Manual: https://www.sms-guard.org/downloads/IPswitch-S0-mini-Anleitung.pdf

![GIF](IPs-S0-mini-2.gif) 
