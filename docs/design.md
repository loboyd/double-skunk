# Design
## Network
A peer-to-peer network will be used to connect players rather than a server-client model. This decision was made largely because P2P networks are interesting. In a trustless system without a central authority however, some interesting security considerations arise (such as how to shuffle and deal cards such that neither peer has access to the other peers cards, or even just how to perform a coin flip to determine the first dealer).
## Peer
In a peer-to-peer network, each peer has the same authortity and responsibility as any other. The responsibilities of a peer in our network are roughly the following: store a few pieces of data such as a player's chosen display name, the win/lose count, etc., maintain a set of previously seen peers, support the network routing protocol, and of course, follow the protocol for a trustless game of cribbage.

For the time being, routing is taking a back burner. As long as peers can manually add each other, two friends can still use the network to play amongst themselves. Playing on a "public" network can come later.

Below is an outline of the procedure that the first version of the peer software will follow when two users are playing against each other:

* connect to a peer 
* exchange info such as display name
* determine the player to get the first crib (using a [cryptographically secure coin flip](https://en.wikipedia.org/wiki/Coin_flipping#Telecommunications))
* game loop
    * deal the cards ([also in a cryptographically secure way](https://en.wikipedia.org/wiki/Mental_poker) -- it seems that a less general version of the SRA Mental Poker protocol could work for the purposes of cribbage)
	* discard in a secure way (also based on ideas from Mental Poker)
	* pegging phase
	* reveal starter card (this might be done before the pegging phase)
	* count hands and crib

## A note about security and development timeline
In an attempt to get *something* working as quickly as possible and keep morale high, the things with security considerations mentioned above will probably be implemented insecurely at first, but in a way that they can be easily swapped with a secure version. For example, the code should be modular enough with respect to the dealing protocol that the insecure protocol directly replaced by the secure protocol with minimal changes to the surrounding code.