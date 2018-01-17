# Project TODO List
Ideally, this document will contain "everything" that should be completed. I put everything in quotes because in general, the further from a particular goal development is, the more abstractly the goal will be described here. Once the first version of the software is complete, the project will probably start using Github's issue system in place of or complementary to this document.

## general
- [ ] Work on P2P communication over the web (either with library or at socket level)
- [x] Consider breaking this file into "player," "functionality," and "main" files -- EDIT -- ended up doing this
- [ ] Write some stand-alone documentation
  - [x] Create this TODO list
  - [ ] Create user/developer documentation (this is a way off at this point, particularly dev docs)
- [ ] Further specify the design (in documention) including networking
## main.py
- [ ] Finish designing the main game loop
- [ ] Write code to initialize networking code once it is implemented
## functionality.py
- [ ] Come up with a nice way of sorting the hands (It would be really nice if the numbers representing the cards happened to share the preferred ordering of the cards -- this way, the native sorted() could be used. -- EDIT -- I think this is working now, but it should probably be double-checked
- [ ] Write a function to count points
  - [ ] Finish design for the score_hand() function
  - [ ] Finish count_run()
  - [ ] Write count_flush()
  - [ ] Write unit tests for all functions called from score_hand()
## player.py
- [ ] Write peg() method