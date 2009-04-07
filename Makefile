

install:
	install -D umts_functions ${prefix}/usr/lib/umts_functions
	install -D umtsd ${prefix}/vsys/umtsd
	install -D 96-umts-tools.rules ${prefix}/etc/udev/rules.d/96-umts-tools.rules
	#install -D umts.init ${prefix}/etc/rc.d/init.d/umts

clean:
	find . -name "*~" -exec rm \{} \;
