#!/bin/bash

username=${SUDO_USER:-${USER}}

chown -R $username:$username /opt/password_king/

