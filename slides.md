<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #1a2a6c, #b21f1f, #fdbb2d)" -->

# Mira

### Who do you think you are?

Note: Welcome to the Mira presentation


### Initial Server Setup
```terminal
casper@juno:~/mira/presentation$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```


### First Connection Attempt
```terminal
127.0.0.1 - - [22/Jun/2025 11:18:42] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Jun/2025 11:18:42] "GET /slides.md HTTP/1.1" 200 -
127.0.0.1 - - [22/Jun/2025 11:18:42] code 404, message File not found
127.0.0.1 - - [22/Jun/2025 11:18:42] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [22/Jun/2025 11:18:43] "GET /assets/mira-logo.png HTTP/1.1" 404 -
```


### Subsequent Requests
```terminal
127.0.0.1 - - [22/Jun/2025 11:19:46] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Jun/2025 11:19:47] "GET /slides.md HTTP/1.1" 200 -
127.0.0.1 - - [22/Jun/2025 11:19:47] "GET /assets/mira-logo.png HTTP/1.1" 200 -
```


### Final State
```terminal
127.0.0.1 - - [22/Jun/2025 11:21:47] "GET / HTTP/1.1" 304 -
127.0.0.1 - - [22/Jun/2025 11:21:48] "GET /slides.md HTTP/1.1" 200 -
```

Note: Each slide shows a different stage of the server interaction 