# Immutable Rules

## Rule Limitations
1. Anything not forbidden by the rules is permitted.
2. No rule set may be proposed which inflicts any punishment
   on a player that is worse than losing the game.
3. Points may only be added or removed if the rules
   explicitly call for it.

## End Game Conditions
1. If all players agree to end the game at any point, the
   game ends.
2. If the game ends prematurely, the player with the largest
   number of points wins. If multiple players are tied for
   the largest number of points, the winner is whoever among
   those players is next in the turn order.

## Disputes
1. A player may accuse another player of violating a
   specific rule or rules.
2. Double jeopardy: No player may be accused twice for the
   same violation of a rule.
3. Non-retroactivity: No player may be accused for violating
   a rule, if the rule was not in effect when the alleged
   violation occurred.
4. Statute of Limitations: No player may be accused of a
   rule violation which took place more than two turns ago.
5. Immutable Precedence: When a Mutable and Immutable rule
   are in conflict, the Immutable rule takes precedence.
6. Age Preference: When two rules of the same class
   (Mutable/Immutable) are active at the same time during a
   dispute, the older rule takes precedence.
7. Adjudicating a Dispute: If a player has been accused, a
   majority vote is initiated, and if it passes, the accused
   player must accept the penalty and all players must
   attempt to reverse any actions which were deemed illegal.
   If necessary, the decision should be reflected in an
   out-of-turn rule clarification.
8. Trial by Combat: During a dispute (or after it, up until
   the accused player gets his next turn), the accused may
   call for a Trial by Combat against his accuser. The
   accuser must ask Slackbot "yes or no". If Slackbot
   answers in the negative, the accused is penalized as
   though he lost the duel. If the answer returns positive,
   an actual DUEL initiates between accuser and accused and
   the violation punishment is waived.

-------------------------------------------------------
 
# Mutable Rules
1. All players begin with 1 point. If a player has at least
   10 points more than every other player and a majority of
   players votes that there are no unpunished rule
   violations, then the game ends and that player is the
   winner.
2. Players take turns in an order determined by the order
   specified in the "Turn Order" section. A turn consists of
   one invocation and one turn action, in any order. After
   the last player has taken their turn, the turn order
   repeats. Turn actions may not be taken by any player
   other than the active player, unless explicitly permitted
   elsewhere in the rules.
3. Points are awarded by posting the message "!give
   @username N points" to #nomic and subtracted by posting
   the message "!take N points from @username" to #nomic,
   where "username" is the canonical username of the person
   and "N" is the number of points. The score can be checked
   by posting the message "!most points" or "!list" in
   #nomic or a direct message to @nomicbot. "!usage" will
   tell you other available commands.
5. The current set of rules will be kept at a bitbucket site
   referenced in the channel topic. Rule proposals can
   consist of a link to a fork with the desired rules. Other
   delivery methods are acceptable. If and only if the
   proposal is accepted, the topic will be changed to only
   include a link to the new rules on bitbucket on both
   channels.
6. Out of turn actions: At any point, a player may take one
   of the actions listed in the "Out-of-Turn Actions"
   section.
7. If the rules require a player's points be changed without
   specifying the actor, the active player must change that
   player's points.
8. Each time The Chosen One takes a turn, each Follower of
   The Chosen One gains a point.
9. Each time The Chosen One loses points, The Chosen One may
   transfer one point to The Chosen One from one of the
   Followers of The Chosen One, if any exist.
10. When The Chosen One changes, each Follower ceases to be
    a Follower of The Chosen One and loses one point, for
    blasphemy.
11. All turn actions, invocations, and calls to !end turn
    must take place in the #nomic_turns channel. Only turn
    actions, invocations, calls to !end turn, and changes to
    the topic may occur in #nomic_turns.
12. The active player must end their turn with a call to
    !end turn. The active player must ensure that the state
    of the game and @inventory are in sync before any call
    to !end turn.
13. At the beginning of a new round of Turn Orders (i.e.
    after the last player in the Turn Order), a Slackbot
    Turn begins.
14. Item actions: If a player has 1 or more of any item
    listed in the Item Actions section, the player may take
    any action listed there as an Out of Turn action unless
    the item's rules specify otherwise.
 
## Definitions
1. Ruleset refers to the content of this document and any
   documents it may refer to. 
2. A line is a collection of characters preceded and ended
   by a newline character or the beginning or ending of a
   document.
3. An empty line is a line with no nonwhitespace characters
   in it.
4. A section is a collection of nonempty lines preceded and
   postceded by empty lines or the beginning or ending of a
   document.
5. A section heading is a line beginning with Ã‚Â§ or #.
6. A rule is one of the numbered lines in this document.
7. A commandment is one of the lines in the Book of
   Commandments document that is nonempty and not a section
   heading.
8. A command is a @slackbot, @foodgod, or @bloodgod response
   to an invocation.
9. A turn is the period of time that a player has the
   :shell: and is thus empowered to invoke and perform a
   turn action.
10. A move, or turn phase, refers to either an invocation or
    turn action.
 
## Invocations
1. The sections of the Book of Commandments are tied to
   invocations by their section header.
2. The invocations are defined as follows:
    - SLACKBOT COMMANDS: awaken @slackbot
    - BLOODGOD CURSES: invoke @bloodgod
    - FOODGOD BLESSINGS: embrace @foodgod
 
## Turn Actions
1. Immutable Change: Propose a modification to any and all
   parts of any and all game documents. If the proposal wins
   a unanimous vote, the active player gains 2 points and
   then the proposed changes take effect.
2. Mutable Change: Propose a modification to this document
   and/or The Book of Commandments, without any changes to
   the immutable rules. If the proposal passes a lottery
   vote, the active player gains 1 point and then the
   proposed changes take effect.
3. Duel: Challenge another player to a duel. Give Bloodgod 1
   point.
4. Gift: Give one point to another player of your choosing
   and one point to Foodgod.
5. Blood Sacrifice: Transfer one of your points to Bloodgod.
6. Fealty: Pledge fealty to The Chosen One. You are now
   considered a Follower of The Chosen One.
7. Art: Create a poem, drawing, song, or short story about
   this game and post it in #nomic. If a randomly chosen
   other player likes your creation, gain 2 points.
8. Pass: A randomly chosen other player gains one point.
9. Craft Item: Transfer 3 of your points to the player with
   the least points and receive a Regular Item of your
   choosing.

## Out-of-Turn Actions
1. Immediate rule change: Propose an immediate change to the
   mutable rules. Over the 24 hours following the proposal,
   if any other player approves the change, it will
   temporarily be enacted. If any player vetoes the rule in
   the 24 hour period, regardless of what rule changes have
   been made, the temporary change will be revoked, along
   with any changes caused by the rule. At the end of the 24
   hour period, the rule will automatically become a regular
   mutable rule.
2. Involuntary turn forfeiture: if 24 hours or longer has
   elapsed since the last move has been made, any player may
   invoke involuntary turn forfeiture, which causes the
   currently active player to lose one point and their turn
   to end. Use the command "!force end turn" to end their
   turn.
3. Initiate Dispute: Accuse another of violating a specific
   rule. If the accused does not acquiesce, or if there is a
   confusion about the application of the rule, a "Dispute"
   can be formally initiated. A Dispute requires a defined
   accuser, a defendant, and a reference to a specific rule
   being broken. The accuser must make clear that he is
   initiating a formal dispute in order for it to be put to
   a vote. If the accuser does not announce a vote, the
   dispute is considered informal and has no legal power.
4. Add Player: Propose the addition of a new player to the
   game. If a majority vote passes, the rules will be
   updated to include the new player at the end of the turn
   order and the new player will be granted the HIGHER of
   either 1 point OR two points fewer than the losingest
   player.
5. Rectify: Propose any action necessary to get the game
   into a state that is strictly more correct, as defined by
   the rules. Over the 24 hours following the proposal, if
   any other player approves the action, it will temporarily
   be enacted. If any player vetoes the rule in the 24 hour
   period, regardless of what rule changes have been made,
   the temporary action will be revoked.
6. Force vote: If a vote has been in progress for 6 hours or
   longer, ask Slackbot to vote on behalf of each voter who
   has not yet voted by asking "Slackbot, would [player]
   vote yes or no?". Once Slackbot has answered, this is
   equivalent to the voter in question having voted
   according to Slackbot's answer.
7. End turn: If the active player has no turn actions
   available, they may end their turn prematurely and incur
   a 1 point penalty.
8. Remove Player: If a player has been skipped in the turn
   order twice consecutively, a player may initiate a vote
   to remove the player from the game. This vote passes if
   every player but one approves of it, or if the skipped
   player approves of it.

## Item Actions
- :game_die: - Re-roll any one dice roll you have performed
  during the current turn. Lose 1 :game_die:.
- :bread: - If another player has had points taken from
  them, restore the lost points. If the other player
  chooses, they may express their gratitude by awarding you
  one point for every point that the player restored. Lose 1
  :bread:.
- :lock: - If another player attempts to transfer away your
  possessions, you can choose to use the :lock: to protect a
  single Regular Item from being transferred. The target
  item should be returned to your inventory. Lose 1 :lock:.

## Slackbot Turns
Slackbot turns occur at the beginning of every Turn Order.
Slackbot's randomly selected declarations last for a full
Turn Order (until Slackbot's next turn.) 

## Random Player Selection
1. Issue the command "!owner of random player". @inventory
   will respond with a randomly chosen player.
2. If the rules specify a random "other" player, then
   re-issue the "!owner of random player" command until a
   player other than yourself is chosen.
 
## Lottery Voting
The vote initiator issues the command "!owner of random
:ballot_box_with_ballot:" until @inventory returns a random
player other than the vote initiator. The randomly chosen
player decides whether or not the motion passes.

## Majority Voting
All players vote. If a strict majority of players have voted
to approve, the motion passes.

## Unanimous Voting
All players vote. If everyone votes in favor, the motion
passes.

## Dueling
1. Both players issue the command "/roll 1d20" once and add
   the number of :gun:s they possess to their roll.
    A. If both players roll a 1, both players lose the duel
    and lose 2 points.
    B. If both players roll the same number (except 1), the
    duel initiator wins the duel.
    C. Otherwise, the player with the higher roll wins the
    duel.
2. If there is a winner, transfer 1 point from the loser to
   the winner.

## Penalties
1. Rules Violation: Violating the rules costs the violator 2
   points.
2. Before the penalty is imposed, any player may propose an
   alternative penalty, which will replace the previous
   penalty if a majority vote passes.

## Ascension
If a player would win the game, they may instead: give or
take any number of items from any number of players and/or
rewrite any and all of the rules. The new rules take effect
immediately, without a voting process.

## Locked Items
The items in this section are locked and cannot be given to
or taken from anyone or anything, unless the rules
explicitly call for it. There are two classes of Locked
Items, "Special" and "Regular". 
- Special Items: chosen, :shell:, godhood, player.
- Regular Items: points, :bread:, :game_die:, :gun:,
:ballot_box_with_ballot:

## Book of Commandments
1. Changes to the Book of Commandments are ratified by
   lottery voting.
2. Sections in the Book of Commandments must begin with a
   section header, followed by commandments.
3. If a change to the Book of Commandments has been
   accepted, the player who proposed the change must do all
   the following things:
    A. Post the message "!update commandments [url]", where
    "[url]" is a url that points to a raw text file of the
    commandments. This message may not be used unless the
    url points to the latest version of the Book of
    Commandments that has been approved.
4. The active player must obey any command given by
   @slackbot, @bloodgod, or @foodgod. If a command requires
   no response, the player is considered to have obeyed.
5. The @bloodgod invocation is only available if @bloodgod
   has more than zero points.
6. The @foodgod invocation is only available if @foodgod has
   more than zero points.
 
## Slacktheon
1. Changes to the Slacktheon are ratified by lottery voting.
   Any change to the Slacktheon must be the addition of
   verse to a single book in the Slacktheon.
2. If a change results in more verses to the Book of Food,
   the active player, all ratifying players, and Foodgod
   recieve a point. 
3. If a change results in more verses to the Book of Blood,
   all players except the active player and all ratifying
   players lose a point and Bloodgod gains a point.
