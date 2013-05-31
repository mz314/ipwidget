all:
	zip -r ../ipwidget.zip ./ipwidget
	
install:
	plasmapkg -i ../ipwidget.zip
	
clean:
	rm ../ipwidget.zip
	plasmapkg -r ipwidget
	
preview:
	plasmoidviewer ipwidget