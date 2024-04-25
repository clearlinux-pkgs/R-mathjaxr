#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mathjaxr
Version  : 1.6.0
Release  : 26
URL      : https://cran.r-project.org/src/contrib/mathjaxr_1.6-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mathjaxr_1.6-0.tar.gz
Summary  : Using 'Mathjax' in Rd Files
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0
BuildRequires : buildreq-R

%description
mathjaxr: Using Mathjax in Rd Files
===================================
[![R build status](https://github.com/wviechtb/mathjaxr/workflows/R-CMD-check/badge.svg)](https://github.com/wviechtb/mathjaxr/actions)
[![CRAN Version](https://www.r-pkg.org/badges/version/mathjaxr)](https://CRAN.R-project.org/package=mathjaxr)
![devel Version](https://img.shields.io/badge/devel-1.6--0-brightgreen.svg)

%prep
%setup -q -c -n mathjaxr
cd %{_builddir}/mathjaxr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646065755

%install
export SOURCE_DATE_EPOCH=1646065755
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mathjaxr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mathjaxr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mathjaxr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mathjaxr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mathjaxr/DESCRIPTION
/usr/lib64/R/library/mathjaxr/INDEX
/usr/lib64/R/library/mathjaxr/Meta/Rd.rds
/usr/lib64/R/library/mathjaxr/Meta/features.rds
/usr/lib64/R/library/mathjaxr/Meta/hsearch.rds
/usr/lib64/R/library/mathjaxr/Meta/links.rds
/usr/lib64/R/library/mathjaxr/Meta/nsInfo.rds
/usr/lib64/R/library/mathjaxr/Meta/package.rds
/usr/lib64/R/library/mathjaxr/NAMESPACE
/usr/lib64/R/library/mathjaxr/NEWS.md
/usr/lib64/R/library/mathjaxr/R/mathjaxr
/usr/lib64/R/library/mathjaxr/R/mathjaxr.rdb
/usr/lib64/R/library/mathjaxr/R/mathjaxr.rdx
/usr/lib64/R/library/mathjaxr/doc/R_dark.css
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/a11y/assistive-mml.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/a11y/complexity.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/a11y/explorer.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/a11y/semantic-enrich.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/action.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/all-packages.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/ams.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/amscd.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/autoload.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/bbox.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/boldsymbol.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/braket.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/bussproofs.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/cancel.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/color.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/colorv2.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/configmacros.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/enclose.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/extpfeil.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/html.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/mhchem.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/newcommand.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/noerrors.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/noundefined.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/physics.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/require.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/tagformat.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/textmacros.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/unicode.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/input/tex/extensions/verb.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/tex.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_AMS-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Calligraphic-Bold.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Calligraphic-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Fraktur-Bold.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Fraktur-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Main-Bold.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Main-Italic.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Main-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Math-BoldItalic.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Math-Italic.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Math-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_SansSerif-Bold.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_SansSerif-Italic.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_SansSerif-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Script-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size1-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size2-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size3-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size4-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Typewriter-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Vector-Bold.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Vector-Regular.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Zero.woff
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/output/svg.js
/usr/lib64/R/library/mathjaxr/doc/mathjax/es5/tex-chtml-full.js
/usr/lib64/R/library/mathjaxr/help/AnIndex
/usr/lib64/R/library/mathjaxr/help/aliases.rds
/usr/lib64/R/library/mathjaxr/help/macros/mathjax.Rd
/usr/lib64/R/library/mathjaxr/help/mathjaxr.rdb
/usr/lib64/R/library/mathjaxr/help/mathjaxr.rdx
/usr/lib64/R/library/mathjaxr/help/paths.rds
/usr/lib64/R/library/mathjaxr/html/00Index.html
/usr/lib64/R/library/mathjaxr/html/R.css
