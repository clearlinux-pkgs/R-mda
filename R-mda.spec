#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mda
Version  : 0.5.3
Release  : 50
URL      : https://cran.r-project.org/src/contrib/mda_0.5-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mda_0.5-3.tar.gz
Summary  : Mixture and Flexible Discriminant Analysis
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mda-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
adaptive regression splines (MARS), BRUTO, and vector-response smoothing splines.
	Hastie, Tibshirani and Friedman (2009) "Elements of Statistical Learning (second edition, chap 12)" Springer, New York.

%package lib
Summary: lib components for the R-mda package.
Group: Libraries

%description lib
lib components for the R-mda package.


%prep
%setup -q -c -n mda
cd %{_builddir}/mda

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651760621

%install
export SOURCE_DATE_EPOCH=1651760621
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mda
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mda || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mda/DESCRIPTION
/usr/lib64/R/library/mda/INDEX
/usr/lib64/R/library/mda/Meta/Rd.rds
/usr/lib64/R/library/mda/Meta/data.rds
/usr/lib64/R/library/mda/Meta/features.rds
/usr/lib64/R/library/mda/Meta/hsearch.rds
/usr/lib64/R/library/mda/Meta/links.rds
/usr/lib64/R/library/mda/Meta/nsInfo.rds
/usr/lib64/R/library/mda/Meta/package.rds
/usr/lib64/R/library/mda/NAMESPACE
/usr/lib64/R/library/mda/R/mda
/usr/lib64/R/library/mda/R/mda.rdb
/usr/lib64/R/library/mda/R/mda.rdx
/usr/lib64/R/library/mda/data/ESL.mixture.rda
/usr/lib64/R/library/mda/data/glass.rda
/usr/lib64/R/library/mda/help/AnIndex
/usr/lib64/R/library/mda/help/aliases.rds
/usr/lib64/R/library/mda/help/mda.rdb
/usr/lib64/R/library/mda/help/mda.rdx
/usr/lib64/R/library/mda/help/paths.rds
/usr/lib64/R/library/mda/html/00Index.html
/usr/lib64/R/library/mda/html/R.css
/usr/lib64/R/library/mda/mda-source.zip
/usr/lib64/R/library/mda/ratfor/README
/usr/lib64/R/library/mda/ratfor/bruto.r
/usr/lib64/R/library/mda/ratfor/dcalcvar.r
/usr/lib64/R/library/mda/ratfor/dmarss.r
/usr/lib64/R/library/mda/ratfor/dorthreg.r
/usr/lib64/R/library/mda/ratfor/dqrreg.r
/usr/lib64/R/library/mda/ratfor/mspline.r
/usr/lib64/R/library/mda/ratfor/sknotl.r
/usr/lib64/R/library/mda/ratfor/tmatch.r
/usr/lib64/R/library/mda/tests/testthat.R
/usr/lib64/R/library/mda/tests/testthat/test_example.R
/usr/lib64/R/library/mda/tests/testthat/test_results/mda-0.4-results.RDS

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mda/libs/mda.so
/usr/lib64/R/library/mda/libs/mda.so.avx2
/usr/lib64/R/library/mda/libs/mda.so.avx512
