https://chatgpt.com/share/69a8b2b6-7e60-8011-bc01-aa1d973367f3


/etc/pam.d/gdm-password
auth     requisite      pam_nologin.so
auth     required       pam_env.so
auth     required       pam_permit.so

account  required       pam_unix.so

password required       pam_unix.so

session  required       pam_env.so
session  required       pam_limits.so
session  required       pam_unix.so
session  required       pam_systemd.so

/etc/pam.d/gdm-autologin
auth     required       pam_env.so
auth     required       pam_permit.so

account  required       pam_unix.so

session  required       pam_env.so
session  required       pam_limits.so
session  required       pam_unix.so
session  required       pam_systemd.so

/etc/pam.d/gdm-launch-environment
auth     required       pam_env.so
auth     required       pam_permit.so

account  required       pam_unix.so

session  required       pam_env.so
session  required       pam_limits.so
session  required       pam_unix.so
session  required       pam_systemd.so