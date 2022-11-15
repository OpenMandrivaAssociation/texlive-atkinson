Name:		texlive-atkinson
Version:	64385
Release:	1
Summary:	Support for the Atkinson Hyperlegible family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/atkinson
License:	lppl other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atkinson.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atkinson.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Atkinson Hyperlegible family of fonts, named
after Braille Institute founder, J. Robert Atkinson. What makes
it different from traditional typography design is that it
focuses on letterform distinction to increase character
recognition, ultimately improving readability.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/atkinson
%{_texmfdistdir}/fonts/vf/public/atkinson
%{_texmfdistdir}/fonts/type1/public/atkinson
%{_texmfdistdir}/fonts/tfm/public/atkinson
%{_texmfdistdir}/fonts/opentype/public/atkinson
%{_texmfdistdir}/fonts/map/dvips/atkinson
%{_texmfdistdir}/fonts/enc/dvips/atkinson
%doc %{_texmfdistdir}/doc/fonts/atkinson

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
