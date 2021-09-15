FROM devkitpro/devkitppc

RUN apt-get update -y && apt-get install -y xxd

RUN git clone https://github.com/dimok789/libiosuhax.git

RUN cd libiosuhax && make && make install && cd ../ && rm -r libiosuhax

RUN git clone https://github.com/CafeCentralUI/Hinata-Installer.git

RUN cd Hinata-Installer && mkdir payload

WORKDIR /Hinata-Installer

ENV PAYLOAD=/Hinata-Installer/payload

RUN cd arm_user && make && mv arm_user* ${PAYLOAD}

RUN cd arm_kernel && make && mv arm_kernel* ${PAYLOAD}

RUN cd wupserver && make && mv wupserver* ${PAYLOAD}

CMD ["bash"]