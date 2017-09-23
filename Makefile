.PHONY: po mo

po:
	mkdir -p virtualspace/locale/ru/LC_MESSAGES
	find . -type f \( -iname \*.py -o -iname \*.kv \) | xargs xgettext -L python --output=virtualspace/locale/messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off virtualspace/locale/ru/LC_MESSAGES/messages.po virtualspace/locale/messages.pot

mo:
	mkdir -p virtualspace/locale/ru/LC_MESSAGES
	msgfmt -c -o virtualspace/locale/ru/LC_MESSAGES/messages.mo virtualspace/locale/ru/LC_MESSAGES/messages.po
