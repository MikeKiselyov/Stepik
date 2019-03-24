# Напишите функцию update_dictionary(d, key, value),
# которая принимает на вход словарь 𝑑 и два числа: 𝑘𝑒𝑦 и 𝑣𝑎𝑙𝑢𝑒.
#
# Если ключ 𝑘𝑒𝑦 есть в словаре 𝑑, то добавьте значение 𝑣𝑎𝑙𝑢𝑒 в список,
# который хранится по этому ключу.
# Если ключа 𝑘𝑒𝑦 нет в словаре, то нужно добавить значение в список по ключу 2⋅𝑘𝑒𝑦.
# Если и ключа 2⋅𝑘𝑒𝑦 нет, то нужно добавить ключ 2⋅𝑘𝑒𝑦 в словарь
# и сопоставить ему список из переданного элемента [𝑣𝑎𝑙𝑢𝑒].
#
# Требуется реализовать только эту функцию, кода вне неё не должно быть.
# Функция не должна вызывать внутри себя функции input и print.
#
# Пример работы функции:
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)

sting = '''
The firehouse trembled as a great flight of jet planes whistled a single note across the black morning sky.

Montag blinked. Beatty was looking at him as if he were a museum statue. At any moment, Beatty might rise and walk about him, touching, exploring his guilt and self-consciousness. Guilt? What guilt was that?

"Your play, Montag."

Montag looked at these men whose faces were sunburnt by a thousand real and ten thousand imaginary fires, whose work flushed their cheeks and fevered their eyes. These men who looked steadily into their platinum igniter flames as they lit their eternally burning black pipes. They and their charcoal hair and soot-colored brows and bluish-ash-smeared cheeks where they had shaven close; but their heritage showed. Montag started up, his mouth opened. Had he ever seen a fireman that didn't have black hair, black brows, a fiery face, and a blue-steel shaved but unshaved look? These men were all mirror images of himself! Were all fireman picked then for their looks as well as their proclivities? The color of cinders and ash about them, and the continual smell of burning from their pipes. Captain Beatty there, rising in thunderheads of tobacco smoke, Beatty opening a fresh tobacco packet, crumpling the cellophane into a sound of fire.

Montag looked at the cards in his own hands. "I -- I've been thinking. About the fire last week.  About the man whose library we fixed. What happened to him?"

"They took him screaming off to the asylum."

"He wasn't insane."

Beatty arranged his cards quietly. "Any man's insane who thinks he can fool the government and us."

"I've tried to imagine," said Montag, "just how it would feel. I mean, to have firemen burn our houses and our books."

"We haven't any books."

"But if we did have some."

"You got some?"

Beatty blinked slowly.

"No." Montag gazed beyond them to the wall with the typed lists of a million forbidden books. Their names leapt in fire, burning down the years under his ax and his hose which sprayed not water but kerosene. "No." But in his mind, a cool wind started up and blew out of the ventilator grille at home, softly, softly, chilling his face. And, again, he saw himself in a green park talking to an old man, a very old man, and the wind from the park was cold, too.

Montag hesitated. "Was -- was it always like this?  The firehouse, our work? I mean, well, once upon a  time ..."

"Once upon a time!" Beatty said. "What kind of talk is that?"

Fool, thought Montag to himself, you'll give it away. At the last fire, a book of fairy tales, he'd  glanced at a single line. "I mean," he said, "in the old days, before homes were completely fireproofed --"  Suddenly it seemed a much younger voice was speaking for him. He opened his mouth and it was Clarisse McClellan saying, "Didn't firemen prevent fires rather than stoke them up and get them going?"

"That's rich!" Stoneman and Black drew forth their rule books, which also contained brief histories of the Firemen of America, and laid them out where Montag, though long familiar with them, might read:

Established, 1790, to burn English-influenced books in the Colonies. First Fireman: Benjamin Franklin.

RULE 1. Answer the alarm swiftly. 
2. Start the fire swiftly. 
3. Burn everything. 
4. Report back to firehouse immediately. 
5. Stand alert for other alarms.

Everyone watched Montag. He did not move.

The alarm sounded.

'''

print(sting.strip())
