%global tl_name hyphen-welsh
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Welsh hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-welsh
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-welsh.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Welsh in T1/EC and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-welsh:
welsh loadhyph-cy.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-welsh:
\addlanguage{welsh}{loadhyph-cy.tex}{}{2}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-welsh:
['welsh'] = {
	loader = 'loadhyph-cy.tex',
	lefthyphenmin = 2,
	righthyphenmin = 3,
	synonyms = {  },
	patterns = 'hyph-cy.pat.txt',
},
TL_HYPHEN_EOF
