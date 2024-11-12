
MAKEFLAGS += " --no-print-directory "

ifdef NAME
  CNAME = $(NAME)
  LNAME = $(shell echo "$(NAME)" | tr '[:upper:]' '[:lower:]')
  UNAME = $(shell echo "$(NAME)" | tr '[:lower:]' '[:upper:]')
  YEAR  = date '+%Y'
  NLEN  = $(shell echo $(NAME) | wc -c)
  NDASH = $(shell printf '%$(NLEN)s' | tr " " "-")
  NEQUL = $(shell printf '%$(NLEN)s' | tr " " "=")
  NHASH = $(shell printf '%$(NLEN)s' | tr " " "\#")
  NSTAR = $(shell printf '%$(NLEN)s' | tr " " "*")
endif


define HELP


    NAME=my_module make templatize
        prepares this copy of radical.template to host module radical.<NAME>
		NAME can be CamelCased.

endef

.PHONY: help
help:
	$(info $(HELP))
	@true


.PHONY: templatize
templatize::
ifndef NAME
	@printf "\n\n    Error: no project NAME given!\n"
	@$(MAKE) help
else
	@echo "CNAME: $(CNAME)"
	@echo "LNAME: $(LNAME)"
	@echo "UNAME: $(UNAME)"
	@ find . -name '*###cname###*' -type d |          sed -e "p;s/###cname###/$(CNAME)/" | xargs -r -n2 mv -v
	@ find . -name '*###lname###*' -type d |          sed -e "p;s/###lname###/$(LNAME)/" | xargs -r -n2 mv -v
	@ find . -name '*###uname###*' -type d |          sed -e "p;s/###uname###/$(UNAME)/" | xargs -r -n2 mv -v
	@ find . -name '*###cname###*'   |                sed -e "p;s/###cname###/$(CNAME)/" | xargs -r -n2 mv -v
	@ find . -name '*###lname###*'   |                sed -e "p;s/###lname###/$(LNAME)/" | xargs -r -n2 mv -v
	@ find . -name '*###uname###*'   |                sed -e "p;s/###uname###/$(UNAME)/" | xargs -r -n2 mv -v
	@ grep   -ilr  '###cname###'   * | xargs -n 1 -tr sed -i 's/###cname###/$(CNAME)/g'
	@ grep   -ilr  '###lname###'   * | xargs -n 1 -tr sed -i 's/###lname###/$(LNAME)/g'
	@ grep   -ilr  '###uname###'   * | xargs -n 1 -tr sed -i 's/###uname###/$(UNAME)/g'
	@ grep   -ilr  '###year###'    * | xargs -n 1 -tr sed -i 's/###year###/$(YEAR)/g'
	@ grep   -ilr  '###ndash###'   * | xargs -n 1 -tr sed -i 's/###ndash###/$(NDASH)/g'
	@ grep   -ilr  '###nequl###'   * | xargs -n 1 -tr sed -i 's/###nequl###/$(NEQUL)/g'
	@ grep   -ilr  '###nhash###'   * | xargs -n 1 -tr sed -i 's/###nhash###/$(NHASH)/g'
	@ grep   -ilr  '###nstar###'   * | xargs -n 1 -tr sed -i 's/###nstar###/$(NSTAR)/g'
	@ mv Makefile.in Makefile
	@ # mv .git .git.radical.template
	@ git add bin/radical-###lname###-version
	@ git add docs/source/module_###lname###.rst
	@ git add src/radical/###lname###/
	@ git add tests/unittests/test_###lname###.py
	@ echo "-----------------------------------"
	@ echo "run: git commit -am initial commit'"
	echo "-----------------------------------"

endif


