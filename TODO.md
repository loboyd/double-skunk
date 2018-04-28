# Project TODO List
Ideally, this document will contain "everything" that should be completed. I put everything in quotes because in general, the further from a particular goal development is, the more abstractly the goal will be described here. Once the first version of the software is complete, the project will probably start using Github's issue system in place of or complementary to this document.

## general
- [ ] Work on P2P communication over the web (either with library or at socket level)
- [x] Consider breaking this file into "player," "functionality," and "main" files -- EDIT -- ended up doing this
- [ ] Write some stand-alone documentation
  - [x] Create this TODO list
  - [x] Create design documentation
  - [ ] Create user/developer documentation (this is a way off at this point, particularly dev docs)
- [ ] Further specify the design (in documention) including networking
- [ ] Work on formatting for gameplay, i.e., how and when the console is cleared, the format of the pegging phase
- [ ] Add user commands to documentation
- [ ] Figure out how to maintain a consistent means of connecting to a friend node (as IP address can change). [This](https://bitmessage.org/bitmessage.pdf) might be useful to read.
## main.py
- [ ] Write code to initialize networking code once it is implemented
- [ ] Update clearscreen() to be cross-platform
- [x] Write enter statement
- [x] Write exit_game()
- [x] Write print_commands() for user commands
- [ ] Maintain user command list order
- [x] Write main client loop
- [x] Write display for first dealer
- [ ] Write code for all user commands
  - [ ] add: add a new friend (name, IP address)
  - [ ] friends: see friend list (probably pickled dictionary)
  - [ ] name: edit your username (probably also pickled)
  - [x] new: enter new game
    - [x] outline main game loop
    - [x] implment get_crib() function
    - [x] implement discard() function
    - [x] implement reveal_starter_card() (EDIT: redesigned so this is not necessary)
    - [x] implement pegging_play()
     -[ ] write code to count `last card for 1` point
    - [ ] implement check game over()
  - [x] help: see this list of commands
  - [x] quit: quit game
  - [ ] display running point total during pegging phase
## functionality.py
- [x] Come up with a nice way of sorting the hands (It would be really nice if the numbers representing the cards happened to share the preferred ordering of the cards -- this way, the native sorted() could be used. -- EDIT -- I think this is working now, but it should probably be double-checked
- [ ] Write a function to count points (count hands)
  - [x] Finish design for the score_hand() function
  - [x] Finish pairs()
  - [x] Finish fifteens
  - [x] Finish count_run()  (EDIT: score_runs())
  - [x] Write count_flush()
  - [ ] Write unit tests for all functions called from score_hand()
- [x] implement deal()
- [ ] implement get_crib()
## peer.py
- [ ] implement sanity checking for user input IP address in get_peer_ip()
- [x] implement send()
- [x] implement recv()
## visual.py
- [ ] implement go_message()
- [ ] write game_end_message(winner) function
