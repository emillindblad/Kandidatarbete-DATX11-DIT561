# Use the official Ubuntu base image
FROM ubuntu:22.04



# Update the package list and install necessary packages
RUN apt-get update && \
    apt-get install -y openssh-server && \
    rm -rf /var/lib/apt/lists/*

#Create new user 
RUN useradd -m -s /bin/bash myuser && \
    echo 'myuser:password' | chpasswd

RUN mkdir /home/myuser/app
COPY src/a.out /home/myuser/app/a.out
COPY src/bufferOverflow.c /home/myuser/app/bufferOverflow.c
copy src/flag.txt /home/myuser/app/flag.txt
copy src/password.txt /home/myuser/app/password.txt
RUN chmod 400 /home/myuser/app/flag.txt
RUN chmod 400 /home/myuser/app/password.txt

RUN chown root:root /home/myuser/app/a.out && \
    chmod 4755 /home/myuser/app/a.out 
    
# Configure SSH
RUN mkdir /var/run/sshd && \
    mkdir -p /home/myuser/.ssh && \
    chown myuser:myuser /home/myuser/.ssh && \
    chmod 700 /home/myuser/.ssh && \
    echo 'PermitRootLogin no' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    sed -i 's/^\(session\s\+required\s\+pam_loginuid.so\)/#\1/' /etc/pam.d/sshd

# Expose the SSH port
EXPOSE 22

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]
