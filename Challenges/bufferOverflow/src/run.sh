#!/bin/bash

socat TCP-LISTEN:1337,reuseaddr,fork EXEC:/bufferOverflow

