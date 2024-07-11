FROM        --platform=$TARGETOS/$TARGETARCH debian:stable-slim AS build

LABEL       author="LiddulBOFH"
LABEL		source="https://github.com/liddulbofh/ironcore-eggs"
LABEL		description="Source server image with git and python"

ENV         DEBIAN_FRONTEND=noninteractive
ENV			PATH /usr/local/bin:$PATH

RUN         dpkg --add-architecture i386 \
				&& apt update \
				&& apt upgrade -y \
				&& apt install -y tar curl gcc g++ lib32gcc-s1 libgcc1 libcurl4-gnutls-dev:i386 libcurl4:i386 lib32tinfo6 libtinfo6:i386 lib32z1 lib32stdc++6 libncurses5:i386 libcurl3-gnutls:i386 libsdl2-2.0-0:i386 iproute2 gdb libsdl1.2debian libfontconfig1 telnet net-tools netcat-traditional tzdata wget git python3 \
				&& useradd -m -d /home/container container

RUN         wget http://http.us.debian.org/debian/pool/main/o/openssl/libssl1.1_1.1.1w-0+deb11u1_i386.deb \
				&& dpkg -i libssl1.1_1.1.1w-0+deb11u1_i386.deb

# removed software-properties-common and python3-pip

USER        container
ENV         USER=container HOME=/home/container
WORKDIR     /home/container

COPY        ./entrypoint.sh /entrypoint.sh
CMD         [ "/bin/bash", "/entrypoint.sh" ]