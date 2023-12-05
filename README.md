# DVSC

Damn Vulnerable Software Center (DVSC) is a Python web hacking challenge.

## Goal

Teach the concept of time analysis side-channel attacks and TOCTOUs.

- The first part of this challenge is heavily inspired by [W3Challs' Temporal attack](https://w3challs.com/challenges/web/temporal_attack)

## Todo

<details>
  <summary>Spoiler!</summary>
  </br>

- [X] Website

  - [X] Frontend
    - [X] Look and feel
    - [X] Pages
      - [X] Login
      - [X] Downloads
      - [X] Locked software item
        - [X] Redirect user to token generation service
  - [X] Backend
    - [X] Configurable secrets
    - [X] Time analysis side-channel
      - [X] 404 error debug handler leaking source code
      - [X] Time analysis side-channel password check
      - [X] Hidden debug post parameter to leak page generation time
    - [X] TOCTOU
      - [X] Check supplied token is valid

- [X] Token generation service

  - [X] TOCTOU
    - [X] Listen on TCP socket for commands
    - [X] Declare global
    - [X] Command types
      - [X] pass
        - [X] Sets global
        - [X] Sleeps for cache flush lie (**vulnerable!**)
        - [X] Checks global
        - [X] Returns token or error
      - [X] help \<command\>
        - [X] Sets global to \<command\> (**vulnerable!**)
        - [X] Print help on given command
      - [X] about
        - [X] Fake about for token generator
      - [X] status
        - [X] Status of listening socket and connected clients

- [X] Documentation
  - [X] SETUP Instructions
    - [X] Fast startup script

- [ ] Solution
  - [ ] Python script to perform the side-channel attack
  - [ ] Python script to beat TOCTOU

</details>
