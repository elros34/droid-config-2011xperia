# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device smultron
%define vendor semc

%define vendor_pretty Sony Ericsson
%define device_pretty Xperia Mini

# Community HW adaptations need this
%define community_adaptation 1

%define pixel_ratio 0.5926

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc

