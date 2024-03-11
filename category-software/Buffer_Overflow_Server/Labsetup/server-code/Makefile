FLAGS    = -z execstack -fno-stack-protector
FLAGS_32 = -static -m32
TARGET   = server stack-L1 stack-L2

L1 = 148
L2 = 244

all: $(TARGET)

server: server.c
	gcc -o server server.c

stack-L1: stack.c
	gcc -DBUF_SIZE=$(L1) -DSHOW_FP $(FLAGS) $(FLAGS_32) -o $@ stack.c

stack-L2: stack.c
	gcc -DBUF_SIZE=$(L2) $(FLAGS) $(FLAGS_32) -o $@ stack.c

clean:
	rm -f badfile $(TARGET)

install:
	cp server ../bof-containers
	cp stack-* ../bof-containers

