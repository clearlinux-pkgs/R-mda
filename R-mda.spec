#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mda
Version  : 0.4.10
Release  : 24
URL      : https://cran.r-project.org/src/contrib/mda_0.4-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mda_0.4-10.tar.gz
Summary  : Mixture and Flexible Discriminant Analysis
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mda-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
This is a first shot at porting the Hastie & Tibshirani mda package to
R.  mda and fda with MARS seem to work fine, but bruto is still broken
and segfaults.  Hopefully, this can be fixed soon.

%package lib
Summary: lib components for the R-mda package.
Group: Libraries

%description lib
lib components for the R-mda package.


%prep
%setup -q -c -n mda

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571864356

%install
export SOURCE_DATE_EPOCH=1571864356
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mda/libs/mda.so
/usr/lib64/R/library/mda/libs/mda.so.avx2
/usr/lib64/R/library/mda/libs/mda.so.avx512
