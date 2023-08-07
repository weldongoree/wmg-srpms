# wmg-srpms
Some miscellaneous packaging for Fedora

# Qmidiarp
This fixes a problem where qmidiarp (standalone or lv2) would crash if you attempted to add a sequencer or
LFO. This also builds against pipewire rather than jack purely for my convenience (the results *should* be
the same). The crash fix involves turning off all hardening, so be advised.

# KDevelop-Python

This fixes the non-existence of KDevelop-Python in Fedora 38. I'll be maintaining this for myself for the
foreseeable so I'll go ahead and see what it takes to actually take on a package in Fedora.
