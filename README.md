# DVSC

Damn Vulnerable Software Center (DVSC) is a Python web hacking challenge.

## Goal

Teach the concept of time analysis side-channel attacks and TOCTOUs.

- The first part of this challenge is heavily inspired by [W3Challs' Temporal attack](https://w3challs.com/challenges/web/temporal_attack)

## Todo

<details>
  <summary>Spoiler!</summary>
  </br>

- [ ] Website

  - [ ] Frontend
    - [ ] Look and feel
    - [ ] Pages
      - [ ] Login
      - [ ] Downloads
      - [ ] Locked software item
        - [ ] Redirect user to token generation service
  - [ ] Backend
    - [ ] Configurable secrets
    - [ ] Time analysis side-channel
      - [ ] 404 error debug handler leaking source code
      - [ ] Time analysis side-channel password check
      - [ ] Hidden debug post parameter to leak page generation time
    - [ ] TOCTOU
      - [ ] Check supplied token is valid

- [ ] Token generation service

  - [ ] TOCTOU
    - [ ] Listen on TCP socket for commands
    - [ ] Declare global
    - [ ] Command types
      - [ ] pass
        - [ ] Sets global
        - [ ] Sleeps for cache flush lie (**vulnerable!**)
        - [ ] Checks global
        - [ ] Returns token or error
      - [ ] help \<command\>
        - [ ] Sets global to \<command\> (**vulnerable!**)
        - [ ] Print help on given command
      - [ ] about
        - [ ] Fake about for token generator
      - [ ] status
        - [ ] Status of listening socket and connected clients

- [ ] Solution
  - [ ] Python script to perform the side-channel attack
  - [ ] Python script to beat TOCTOU

</details>
