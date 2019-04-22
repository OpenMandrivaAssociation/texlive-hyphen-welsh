# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-welsh
Version:	20181105
Release:	1
Summary:	Welsh hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-welsh.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Welsh in T1/EC and UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-welsh
%_texmf_language_def_d/hyphen-welsh
%_texmf_language_lua_d/hyphen-welsh

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-welsh <<EOF
\%% from hyphen-welsh:
welsh loadhyph-cy.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-welsh
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-welsh <<EOF
\%% from hyphen-welsh:
\addlanguage{welsh}{loadhyph-cy.tex}{}{2}{3}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-welsh
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-welsh <<EOF
-- from hyphen-welsh:
	['welsh'] = {
		loader = 'loadhyph-cy.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-cy.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767635
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759946
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718687
- texlive-hyphen-welsh
- texlive-hyphen-welsh
- texlive-hyphen-welsh
- texlive-hyphen-welsh

