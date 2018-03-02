output: data.json render.py template.mustache
	python3 render.py

.phony: deploy clean

deploy: output
	scp -r output/* rcmarcus@diadem.cs.brandeis.edu:~/.www/seminars/

clean:
	rm -rf output
