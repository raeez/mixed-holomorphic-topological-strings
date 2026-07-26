# ----------------------------------------------------------------------------
# -- Config

# -- meta data
AUTHOR :=Raeez Lorgat

# -- project files and directories
TEXMAIN      :=main
TEXSUITEMAIN :=$(TEXMAIN).tex.latexmain
BIB          :=bib
SECTIONS     :=sections

# -- preferred readers
PDFVIEWER  :=Skim
HTMLVIEWER :=Safari
VIEWPDF    :=open -a $(PDFVIEWER)
VIEWHTML   :=open -a $(HTMLVIEWER)

# -- target dirs for generated html/pdf files
INSTALLURL :=notes/wip
INSTALLDIR :=$(PROJ)/www/raeez.com/$(INSTALLURL)
OUTDIR:=out
LOGDIR:=.build_logs
ICLOUD_DIR :=/Users/raeez/Library/Mobile Documents/com~apple~CloudDocs/research

# -- mathematics publish dir: release binary copied here under canonical name
MATHEMATICS_DIR :=$(HOME)/mathematics
PUBLISHED_PDF   :=mixed-holomorphic-topological-strings.pdf
VOLUME_KEY      :=mixed
PYTHON_BIN      :=python3

# -- pdf config
LTXDIR        :=$(shell kpsewhich -var-value=TEXMFHOME)
TEXFLAGS      :=-output-directory=out -interaction=nonstopmode
TEX           :=pdflatex $(TEXFLAGS)
BUILDTEX      :=$(TEX) $(TEXMAIN).tex
QUICKBUILDTEX :=$(TEX) $(TEXFLAGS) $(TEXMAIN).tex
TEXDEBRIS     :=*.aux *.bbl *.bcf *.blg *.brf *.dvi *.fdb_latexmk *.fls *.gla *.idx *.ilg *.ind *.log *.nlo *.nls *.out *.run.xml *.sta *.synctex.gz *.tar.gz *.toc
STANDALONE_TEX :=$(wildcard standalone/*.tex)
STANDALONE_PASSES :=3
STANDALONE_TEXENGINE :=pdflatex
STANDALONE_TEXFLAGS :=-interaction=nonstopmode -file-line-error -synctex=0

# -- html config
HTMLTARGET :=--css-filename $(TEXMAIN).css --dest-dir $(OUTDIR)
HTMLFLAGS  :=--embed-javascript 0 --embed-css 0 --embed-image 0 $(HTMLTARGET)
HTMLFONTS  :="Karla", "Courier New"
BUILDHTML  :=pdf2htmlex $(HTMLFLAGS)

PDF2HTMLEXJSFILENAME :=pdf2htmlEX.min.js
GOOGLEANALYTICSID    :=UA-8883032-10
define STATICPDFHTML
<head><meta charset="utf-8"><meta name="Description" content="Closed Hamiltonian BF Theory as a Derived Poisson Centre" /><title>Raeez Lorgat</title><meta name="author" content="Raeez Lorgat"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="google-site-verification" content="WfuYCzFoftKafLhmWLqacdDaXEsU4EKbRyZnEwLFxQw" /><link rel="stylesheet" href="scale.css"><!--<script src="jquery-2.1.0.min.js"></script>--><script src="modernizr-2.0.6.min.js"></script><meta http-equiv="refresh" content="0; url=http://raeez.com/$(INSTALLURL)/$(TEXMAIN)/$(TEXMAIN).pdf" /> </head>
endef

define STATICJAVASCRIPT
(function(){/*
 https://github.com/coolwanglu/pdf2htmlEX/blob/master/share/LICENSE
*/
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  ga('create', '$(GOOGLEANALYTICSID)', 'raeez.com');
  ga('send', 'pageview');
  $(window).load(function(){
   $('.containerIMG').find('img').each(function(){
    var imgClass = (this.width/this.height > 1) ? 'wide' : 'tall';
    $(this).addClass(imgClass);
   })
  })
var pdf2htmlEX=window.pdf2htmlEX=window.pdf2htmlEX||{},CSS_CLASS_NAMES={page_frame:"pf",page_content_box:"pc",page_data:"pi",background_image:"bi",link:"l",input_radio:"ir",__dummy__:"no comma"},DEFAULT_CONFIG={container_id:"page-container",sidebar_id:"sidebar",outline_id:"outline",loading_indicator_cls:"loading-indicator",preload_pages:3,render_timeout:100,scale_step:0.9,key_handler:!0,hashchange_handler:!0,view_history_handler:!0,__dummy__:"no comma"},EPS=1E-6;
function invert(a){var b=a[0]*a[3]-a[1]*a[2];return[a[3]/b,-a[1]/b,-a[2]/b,a[0]/b,(a[2]*a[5]-a[3]*a[4])/b,(a[1]*a[4]-a[0]*a[5])/b]}function transform(a,b){return[a[0]*b[0]+a[2]*b[1]+a[4],a[1]*b[0]+a[3]*b[1]+a[5]]}function get_page_number(a){return parseInt(a.getAttribute("data-page-no"),16)}function disable_dragstart(a){for(var b=0,c=a.length;b<c;++b)a[b].addEventListener("dragstart",function(){return!1},!1)}
function clone_and_extend_objs(a){for(var b={},c=0,e=arguments.length;c<e;++c){var h=arguments[c],d;for(d in h)h.hasOwnProperty(d)&&(b[d]=h[d])}return b}
function Page(a){if(a){this.shown=this.loaded=!1;this.page=a;this.num=get_page_number(a);this.original_height=a.clientHeight;this.original_width=a.clientWidth;var b=a.getElementsByClassName(CSS_CLASS_NAMES.page_content_box)[0];b&&(this.content_box=b,this.original_scale=this.cur_scale=this.original_height/b.clientHeight,this.page_data=JSON.parse(a.getElementsByClassName(CSS_CLASS_NAMES.page_data)[0].getAttribute("data-data")),this.ctm=this.page_data.ctm,this.ictm=invert(this.ctm),this.loaded=!0)}}
Page.prototype={hide:function(){this.loaded&&this.shown&&(this.content_box.classList.remove("opened"),this.shown=!1)},show:function(){this.loaded&&!this.shown&&(this.content_box.classList.add("opened"),this.shown=!0)},rescale:function(a){this.cur_scale=0===a?this.original_scale:a;this.loaded&&(a=this.content_box.style,a.msTransform=a.webkitTransform=a.transform="scale("+this.cur_scale.toFixed(3)+")");a=this.page.style;a.height=this.original_height*this.cur_scale+"px";a.width=this.original_width*this.cur_scale+
"px"},view_position:function(){var a=this.page,b=a.parentNode;return[b.scrollLeft-a.offsetLeft-a.clientLeft,b.scrollTop-a.offsetTop-a.clientTop]},height:function(){return this.page.clientHeight},width:function(){return this.page.clientWidth}};function Viewer(a){this.config=clone_and_extend_objs(DEFAULT_CONFIG,0<arguments.length?a:{});this.pages_loading=[];this.init_before_loading_content();var b=this;document.addEventListener("DOMContentLoaded",function(){b.init_after_loading_content()},!1)}
Viewer.prototype={scale:1,cur_page_idx:0,first_page_idx:0,init_before_loading_content:function(){this.pre_hide_pages()},initialize_radio_button:function(){for(var a=document.getElementsByClassName(CSS_CLASS_NAMES.input_radio),b=0;b<a.length;b++)a[b].addEventListener("click",function(){this.classList.toggle("checked")})},init_after_loading_content:function(){this.sidebar=document.getElementById(this.config.sidebar_id);this.outline=document.getElementById(this.config.outline_id);this.container=document.getElementById(this.config.container_id);
this.loading_indicator=document.getElementsByClassName(this.config.loading_indicator_cls)[0];for(var a=!0,b=this.outline.childNodes,c=0,e=b.length;c<e;++c)if("ul"===b[c].nodeName.toLowerCase()){a=!1;break}a||this.sidebar.classList.add("opened");this.find_pages();if(0!=this.pages.length){disable_dragstart(document.getElementsByClassName(CSS_CLASS_NAMES.background_image));this.config.key_handler&&this.register_key_handler();var h=this;this.config.hashchange_handler&&window.addEventListener("hashchange",
function(a){h.navigate_to_dest(document.location.hash.substring(1))},!1);this.config.view_history_handler&&window.addEventListener("popstate",function(a){a.state&&h.navigate_to_dest(a.state)},!1);this.container.addEventListener("scroll",function(){h.update_page_idx();h.schedule_render(!0)},!1);[this.container,this.outline].forEach(function(a){a.addEventListener("click",h.link_handler.bind(h),!1)});this.initialize_radio_button();this.render()}},find_pages:function(){for(var a=[],b={},c=this.container.childNodes,
e=0,h=c.length;e<h;++e){var d=c[e];d.nodeType===Node.ELEMENT_NODE&&d.classList.contains(CSS_CLASS_NAMES.page_frame)&&(d=new Page(d),a.push(d),b[d.num]=a.length-1)}this.pages=a;this.page_map=b},load_page:function(a,b,c){var e=this.pages;if(!(a>=e.length||(e=e[a],e.loaded||this.pages_loading[a]))){var e=e.page,h=e.getAttribute("data-page-url");if(h){this.pages_loading[a]=!0;var d=e.getElementsByClassName(this.config.loading_indicator_cls)[0];"undefined"===typeof d&&(d=this.loading_indicator.cloneNode(!0),
d.classList.add("active"),e.appendChild(d));var f=this,g=new XMLHttpRequest;g.open("GET",h,!0);g.onload=function(){if(200===g.status||0===g.status){var b=document.createElement("div");b.innerHTML=g.responseText;for(var d=null,b=b.childNodes,e=0,h=b.length;e<h;++e){var p=b[e];if(p.nodeType===Node.ELEMENT_NODE&&p.classList.contains(CSS_CLASS_NAMES.page_frame)){d=p;break}}b=f.pages[a];f.container.replaceChild(d,b.page);b=new Page(d);f.pages[a]=b;b.hide();b.rescale(f.scale);disable_dragstart(d.getElementsByClassName(CSS_CLASS_NAMES.background_image));
f.schedule_render(!1);c&&c(b)}delete f.pages_loading[a]};g.send(null)}void 0===b&&(b=this.config.preload_pages);0<--b&&(f=this,setTimeout(function(){f.load_page(a+1,b)},0))}},pre_hide_pages:function(){var a="@media screen{."+CSS_CLASS_NAMES.page_content_box+"{display:none;}}",b=document.createElement("style");b.styleSheet?b.styleSheet.cssText=a:b.appendChild(document.createTextNode(a));document.head.appendChild(b)},render:function(){for(var a=this.container,b=a.scrollTop,c=a.clientHeight,a=b-c,b=
b+c+c,c=this.pages,e=0,h=c.length;e<h;++e){var d=c[e],f=d.page,g=f.offsetTop+f.clientTop,f=g+f.clientHeight;g<=b&&f>=a?d.loaded?d.show():this.load_page(e):d.hide()}},update_page_idx:function(){var a=this.pages,b=a.length;if(!(2>b)){for(var c=this.container,e=c.scrollTop,c=e+c.clientHeight,h=-1,d=b,f=d-h;1<f;){var g=h+Math.floor(f/2),f=a[g].page;f.offsetTop+f.clientTop+f.clientHeight>=e?d=g:h=g;f=d-h}this.first_page_idx=d;for(var g=h=this.cur_page_idx,k=0;d<b;++d){var f=a[d].page,l=f.offsetTop+f.clientTop,
f=f.clientHeight;if(l>c)break;f=(Math.min(c,l+f)-Math.max(e,l))/f;if(d===h&&Math.abs(f-1)<=EPS){g=h;break}f>k&&(k=f,g=d)}this.cur_page_idx=g}},schedule_render:function(a){if(void 0!==this.render_timer){if(!a)return;clearTimeout(this.render_timer)}var b=this;this.render_timer=setTimeout(function(){delete b.render_timer;b.render()},this.config.render_timeout)},register_key_handler:function(){var a=this;window.addEventListener("DOMMouseScroll",function(b){if(b.ctrlKey){b.preventDefault();var c=a.container,
e=c.getBoundingClientRect(),c=[b.clientX-e.left-c.clientLeft,b.clientY-e.top-c.clientTop];a.rescale(Math.pow(a.config.scale_step,b.detail),!0,c)}},!1);window.addEventListener("keydown",function(b){var c=!1,e=b.ctrlKey||b.metaKey,h=b.altKey;switch(b.keyCode){case 61:case 107:case 187:e&&(a.rescale(1/a.config.scale_step,!0),c=!0);break;case 173:case 109:case 189:e&&(a.rescale(a.config.scale_step,!0),c=!0);break;case 48:e&&(a.rescale(0,!1),c=!0);break;case 33:h?a.scroll_to(a.cur_page_idx-1):a.container.scrollTop-=
a.container.clientHeight;c=!0;break;case 34:h?a.scroll_to(a.cur_page_idx+1):a.container.scrollTop+=a.container.clientHeight;c=!0;break;case 35:a.container.scrollTop=a.container.scrollHeight;c=!0;break;case 36:a.container.scrollTop=0,c=!0}c&&b.preventDefault()},!1)},rescale:function(a,b,c){var e=this.scale;this.scale=a=0===a?1:b?e*a:a;c||(c=[0,0]);b=this.container;c[0]+=b.scrollLeft;c[1]+=b.scrollTop;for(var h=this.pages,d=h.length,f=this.first_page_idx;f<d;++f){var g=h[f].page;if(g.offsetTop+g.clientTop>=
c[1])break}g=f-1;0>g&&(g=0);var g=h[g].page,k=g.clientWidth,f=g.clientHeight,l=g.offsetLeft+g.clientLeft,m=c[0]-l;0>m?m=0:m>k&&(m=k);k=g.offsetTop+g.clientTop;c=c[1]-k;0>c?c=0:c>f&&(c=f);for(f=0;f<d;++f)h[f].rescale(a);b.scrollLeft+=m/e*a+g.offsetLeft+g.clientLeft-m-l;b.scrollTop+=c/e*a+g.offsetTop+g.clientTop-c-k;this.schedule_render(!0)},fit_width:function(){var a=this.cur_page_idx;this.rescale(this.container.clientWidth/this.pages[a].width(),!0);this.scroll_to(a)},fit_height:function(){var a=this.cur_page_idx;
this.rescale(this.container.clientHeight/this.pages[a].height(),!0);this.scroll_to(a)},get_containing_page:function(a){for(;a;){if(a.nodeType===Node.ELEMENT_NODE&&a.classList.contains(CSS_CLASS_NAMES.page_frame)){a=get_page_number(a);var b=this.page_map;return a in b?this.pages[b[a]]:null}a=a.parentNode}return null},link_handler:function(a){var b=a.target,c=b.getAttribute("data-dest-detail");if(c){if(this.config.view_history_handler)try{var e=this.get_current_view_hash();window.history.replaceState(e,
"","#"+e);window.history.pushState(c,"","#"+c)}catch(h){}this.navigate_to_dest(c,this.get_containing_page(b));a.preventDefault()}},navigate_to_dest:function(a,b){try{var c=JSON.parse(a)}catch(e){return}if(c instanceof Array){var h=c[0],d=this.page_map;if(h in d){for(var f=d[h],h=this.pages[f],d=2,g=c.length;d<g;++d){var k=c[d];if(null!==k&&"number"!==typeof k)return}for(;6>c.length;)c.push(null);var g=b||this.pages[this.cur_page_idx],d=g.view_position(),d=transform(g.ictm,[d[0],g.height()-d[1]]),
g=this.scale,l=[0,0],m=!0,k=!1,n=this.scale;switch(c[1]){case "XYZ":l=[null===c[2]?d[0]:c[2]*n,null===c[3]?d[1]:c[3]*n];g=c[4];if(null===g||0===g)g=this.scale;k=!0;break;case "Fit":case "FitB":l=[0,0];k=!0;break;case "FitH":case "FitBH":l=[0,null===c[2]?d[1]:c[2]*n];k=!0;break;case "FitV":case "FitBV":l=[null===c[2]?d[0]:c[2]*n,0];k=!0;break;case "FitR":l=[c[2]*n,c[5]*n],m=!1,k=!0}if(k){this.rescale(g,!1);var p=this,c=function(a){l=transform(a.ctm,l);m&&(l[1]=a.height()-l[1]);p.scroll_to(f,l)};h.loaded?
c(h):(this.load_page(f,void 0,c),this.scroll_to(f))}}}},scroll_to:function(a,b){var c=this.pages;if(!(0>a||a>=c.length)){c=c[a].view_position();void 0===b&&(b=[0,0]);var e=this.container;e.scrollLeft+=b[0]-c[0];e.scrollTop+=b[1]-c[1]}},get_current_view_hash:function(){var a=[],b=this.pages[this.cur_page_idx];a.push(b.num);a.push("XYZ");var c=b.view_position(),c=transform(b.ictm,[c[0],b.height()-c[1]]);a.push(c[0]/this.scale);a.push(c[1]/this.scale);a.push(this.scale);return JSON.stringify(a)}};
pdf2htmlEX.Viewer=Viewer;})();
endef

# -- tar config
TARCONTENTS := README.md Makefile *.tex $(TEXSUITEMAIN) $(BIB) $(SECTIONS)

# -- utils
MKDIR :=mkdir -p
ECHO  :=echo
KILL  :=rm -rf
CP    :=cp
MV    :=mv -f
CD    :=cd
TAR   :=tar

# -- timestamp
NOW := $(shell date +"%c" | tr ' :' '__')

# ----------------------------------------------------------------------------
# -- default and meta build rules
#
.DEFAULT_GOAL := platonic

.PHONY: platonic all quick fast release standalone icloud help mathematics-publish root-publish architecture unified-architecture
quick:
	$(MKDIR) $(OUTDIR)
	$(QUICKBUILDTEX)
	-open $(OUTDIR)/$(TEXMAIN).pdf  # leading hyphen: tolerate headless / no-GUI failure

fast: quick

all: clean pdf html tar install

release:
	$(MKDIR) $(OUTDIR) $(LOGDIR)
	@echo ""
	@echo "  =========================================="
	@echo "  -- COMPLETE BUILD (topological strings) --"
	@echo "  =========================================="
	@echo ""
	@echo "  [1/4] Paper, standalone documents and iCloud"
	@$(MAKE) --no-print-directory icloud
	@echo ""
	@echo "  [2/4] Publish to repo root (canonical PDF name)"
	@$(MAKE) --no-print-directory root-publish
	@echo ""
	@echo "  [3/4] Publish to ~/mathematics + per-volume architecture"
	@$(MAKE) --no-print-directory mathematics-publish
	@$(MAKE) --no-print-directory architecture
	@echo ""
	@echo "  [4/4] Cross-volume architecture aggregation"
	@$(MAKE) --no-print-directory unified-architecture
	@echo ""
	@echo "  =========================================="
	@echo "  Build complete. All output in out/:"
	@ls -1 $(OUTDIR)/*.pdf 2>/dev/null | sed 's/^/    /'
	@echo "  =========================================="

## platonic: Build the integrated monograph -> out/platonic.pdf
##   The state-of-the-art root: the shared five-volume spine plus the merged
##   audit and obstruction chapters.  See platonic/PLATONIC_LEDGER.md.
platonic:
	@echo "  -- Building the integrated monograph --"
	@mkdir -p out .build_logs
	@cd platonic && \
	  TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	  pdflatex -interaction=nonstopmode -file-line-error main.tex >../.build_logs/platonic.log 2>&1 || true; \
	  TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	  bibtex main >>../.build_logs/platonic.log 2>&1 || true; \
	  for i in 1 2 3; do \
	    TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	    pdflatex -interaction=nonstopmode -file-line-error main.tex >../.build_logs/platonic.log 2>&1 || true; \
	  done
	@if [ -f platonic/main.pdf ]; then \
		cp platonic/main.pdf out/platonic.pdf; \
		echo "    OK out/platonic.pdf ($$(pdfinfo platonic/main.pdf 2>/dev/null | awk '/^Pages/{print $$2}') pages)"; \
	else echo "    FAIL - see .build_logs/platonic.log"; exit 1; fi
	@if grep -aqE '^! ' .build_logs/platonic.log; then \
		echo "    LaTeX errors:"; grep -aE '^! ' .build_logs/platonic.log | head -5; exit 1; fi
	@if grep -aqE 'Reference .* undefined|Citation .* undefined' .build_logs/platonic.log; then \
		echo "    undefined references or citations:"; \
		grep -aE 'Reference .* undefined|Citation .* undefined' .build_logs/platonic.log | head -5; exit 1; fi
	@echo "    0 errors, 0 undefined references, 0 undefined citations."


## root-publish: Copy the release binary to repo root under its canonical name
root-publish:
	@if [ -f "$(OUTDIR)/$(TEXMAIN).pdf" ]; then \
		$(CP) "$(OUTDIR)/$(TEXMAIN).pdf" "$(PUBLISHED_PDF)"; \
		echo "    ok  $(PUBLISHED_PDF) (in repo root)"; \
	else \
		echo "    fail  $(OUTDIR)/$(TEXMAIN).pdf missing -- skipping root publish"; \
	fi

## mathematics-publish: Copy the release binary to ~/mathematics under its canonical name
mathematics-publish:
	@$(MKDIR) "$(MATHEMATICS_DIR)"
	@if [ -f "$(OUTDIR)/$(TEXMAIN).pdf" ]; then \
		$(CP) "$(OUTDIR)/$(TEXMAIN).pdf" "$(MATHEMATICS_DIR)/$(PUBLISHED_PDF)"; \
		echo "    ok  $(MATHEMATICS_DIR)/$(PUBLISHED_PDF)"; \
	else \
		echo "    fail  $(OUTDIR)/$(TEXMAIN).pdf missing -- skipping ~/mathematics publish"; \
	fi

## architecture: Build interactive HTML + JSON of the manuscript architecture
architecture:
	@$(PYTHON_BIN) scripts/build_architecture.py --root . --volume $(VOLUME_KEY) --out $(OUTDIR) --quiet
	@$(MKDIR) "$(MATHEMATICS_DIR)/architecture"
	@$(CP) "$(OUTDIR)/architecture.json" "$(MATHEMATICS_DIR)/architecture/$(VOLUME_KEY).json"
	@echo "    ok  $(OUTDIR)/architecture.html + .json"
	@echo "    ok  $(MATHEMATICS_DIR)/architecture/$(VOLUME_KEY).json"

## unified-architecture: Aggregate all per-volume architecture.json into the cross-volume HTML+JSON
unified-architecture:
	@$(PYTHON_BIN) scripts/build_unified_architecture.py --mathematics-dir "$(MATHEMATICS_DIR)" --quiet
	@echo "    ok  $(MATHEMATICS_DIR)/architecture.html + .json"

standalone:
	@echo "  -- Building standalone documents --"
	@$(MKDIR) $(OUTDIR) $(LOGDIR)
	@if [ -z "$(strip $(STANDALONE_TEX))" ]; then \
		echo "  (no standalone documents found)"; \
	else \
		failures=0; \
		for tex in $(STANDALONE_TEX); do \
			if [ ! -f "$$tex" ]; then continue; fi; \
			base=$$(basename "$$tex" .tex); \
			if [ -f "$(OUTDIR)/$$base.pdf" ] && [ "$(OUTDIR)/$$base.pdf" -nt "$$tex" ]; then \
				echo "  ok  $(OUTDIR)/$$base.pdf (up to date)"; \
				continue; \
			fi; \
			tmpdir=$$(mktemp -d "/tmp/mkd-$$(basename "$$(pwd)")-standalone-$$base.XXXXXX"); \
			echo "  [standalone] $$tex -> $(OUTDIR)/$$base.pdf"; \
			for pass in $$(seq 1 $(STANDALONE_PASSES)); do \
				TEXINPUTS="$$tmpdir:$$(pwd):$$(pwd)/standalone:" $(STANDALONE_TEXENGINE) $(STANDALONE_TEXFLAGS) -output-directory="$$tmpdir" "$$tex" >"$(LOGDIR)/standalone-$$base-pass$$pass.log" 2>&1; rc=$$?; \
				if [ -f "$$tmpdir/$$base.idx" ]; then makeindex -q "$$tmpdir/$$base.idx" >/dev/null 2>&1 || true; fi; \
				if [ $$rc -ne 0 ]; then \
					if grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$(LOGDIR)/standalone-$$base-pass$$pass.log" >/dev/null 2>&1; then \
						echo "  fail  $$tex failed on pass $$pass. See $(LOGDIR)/standalone-$$base-pass$$pass.log"; \
						grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$(LOGDIR)/standalone-$$base-pass$$pass.log" | head -n 20 || tail -n 40 "$(LOGDIR)/standalone-$$base-pass$$pass.log"; \
						failures=$$((failures + 1)); \
						break; \
					else \
						echo "  warn  $$tex returned $$rc on pass $$pass; continuing."; \
					fi; \
				fi; \
			done; \
			if [ -f "$$tmpdir/$$base.pdf" ]; then \
				$(CP) "$$tmpdir/$$base.pdf" "$(OUTDIR)/$$base.pdf"; \
				echo "  ok  $(OUTDIR)/$$base.pdf"; \
			elif [ $$failures -eq 0 ]; then \
				echo "  fail  no PDF produced for $$tex"; \
				failures=$$((failures + 1)); \
			fi; \
		done; \
		if [ $$failures -ne 0 ]; then \
			echo "  fail  $$failures standalone document(s) failed."; \
			exit 1; \
		fi; \
	fi

icloud: pdf standalone
	@echo "  -- Copying topological strings PDFs to iCloud --"
	@$(MKDIR) "$(ICLOUD_DIR)/topological_strings"
	@[ -f "$(OUTDIR)/$(TEXMAIN).pdf" ] || { echo "  fail  missing $(OUTDIR)/$(TEXMAIN).pdf"; exit 1; }
	@$(CP) "$(OUTDIR)/$(TEXMAIN).pdf" "$(ICLOUD_DIR)/topological_strings/topological_strings.pdf"
	@echo "    ok  topological_strings/topological_strings.pdf"
	@for pdf in $(OUTDIR)/*.pdf; do \
		[ -e "$$pdf" ] || continue; \
		name=$$(basename "$$pdf"); \
		if [ "$$name" != "$(TEXMAIN).pdf" ]; then \
			$(CP) "$$pdf" "$(ICLOUD_DIR)/topological_strings/$$name"; \
			echo "    ok  topological_strings/$$name"; \
		fi; \
	done
	@echo "  Topological strings PDFs copied to iCloud."

help:
	@echo ""
	@echo "  Topological strings -- Build System"
	@echo "  ------------------------------------"
	@echo "  make            Full legacy build"
	@echo "  make fast       Quick PDF build"
	@echo "  make release    Full rebuild -> out/ + standalones + iCloud"
	@echo "  make standalone Build standalone documents -> out/"
	@echo "  make icloud     Build and copy PDFs to iCloud Drive"
	@echo "  make clean      Remove build debris"
	@echo "  make help       This message"
	@echo ""

# ----------------------------------------------------------------------------
# -- view output
#
.PHONY: open-pdf open-html
open: open-pdf open-html

open-pdf:
	-$(VIEWPDF) out/$(TEXMAIN).pdf

open-html:
	-$(VIEWHTML) out/$(TEXMAIN).html

# ----------------------------------------------------------------------------
# -- quick pdf generation
#

.PHONY: qc q qall
qc: clean quick index

q: qall # aliases to qall
qall: clean
	-make index
	-$(QUICKBUILDTEX)

# ----------------------------------------------------------------------------
# -- build pdf and html
#
.PHONY: pdf html index
p:
	$(BUILDTEX)

pdf:
	$(MKDIR) $(OUTDIR)
	$(BUILDTEX)
	$(MAKE) index
	$(BUILDTEX)
	$(BUILDTEX)
	$(BUILDTEX)
	$(MAKE) index
	$(BUILDTEX)
	$(BUILDTEX)
	$(BUILDTEX)
	@[ -f "$(OUTDIR)/$(TEXMAIN).pdf" ] || { echo "  fail  missing $(OUTDIR)/$(TEXMAIN).pdf"; exit 1; }


index:
	@if [ -f "$(OUTDIR)/$(TEXMAIN).nlo" ]; then \
		makeindex "$(OUTDIR)/$(TEXMAIN).nlo" -s nomencl.ist -o "$(OUTDIR)/$(TEXMAIN).nls"; \
	else \
		echo "  (no nomenclature file: $(OUTDIR)/$(TEXMAIN).nlo)"; \
	fi

html:
	$(BUILDHTML) $(OUTDIR)/$(TEXMAIN).pdf

# ----------------------------------------------------------------------------
# -- install
.PHONY: install install-pdf install-html intall-tar

tar:
	$(TAR) cvzf $(OUTDIR)/$(TEXMAIN)-$(NOW).tar.gz $(TARCONTENTS)

install: install-pdf install-html install-tar

install-pdf:
	-$(MKDIR) $(INSTALLDIR)/$(TEXMAIN)
	-$(CD) $(INSTALLDIR)/$(TEXMAIN); $(KILL) *.pdf; cd -
	$(CD) $(OUTDIR); $(CP) $(TEXMAIN).pdf $(INSTALLDIR)/$(TEXMAIN)/; cd -
	$(ECHO) "$(STATICPDFHTML)" >> $(INSTALLDIR)/$(TEXMAIN)/$(TEXMAIN).pdf.html
	$(CD) $(PROJ)/www/raeez.com; make update-mathematica

install-html:
	-$(MKDIR) $(INSTALLDIR)/$(TEXMAIN)
	-$(CD) $(INSTALLDIR)/$(TEXMAIN); $(KILL) *.css *.js *.png *.js; cd -
	$(CD) $(OUTDIR); $(CP) *.html *.css *.js *.png $(INSTALLDIR)/$(TEXMAIN)/; cd -
	$(CD) $(PROJ)/www/raeez.com; make update-mathematica

# ----------------------------------------------------------------------------
# -- clean
.PHONY: clean
clean:
	-$(KILL) $(TEXDEBRIS)
	-$(CD) $(OUTDIR); $(KILL) $(TEXDEBRIS)
