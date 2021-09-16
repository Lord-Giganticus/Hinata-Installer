FROM devkitpro/devkitppc

RUN apt-get update -y && apt-get install -y xxd

RUN git clone https://github.com/dimok789/libiosuhax.git

RUN cd libiosuhax && make && make install && cd ../ && rm -r libiosuhax

RUN mkdir Hinata-Installer

WORKDIR /Hinata-Installer

RUN mkdir payload

ENV PAYLOAD=/Hinata-Installer/payload

COPY . .

RUN cd arm_user && make && mv arm_user* ${PAYLOAD}

RUN cd arm_kernel && make && mv arm_kernel* ${PAYLOAD}

RUN cd wupserver && make && mv wupserver* ${PAYLOAD}

CMD ["bash"]