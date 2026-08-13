%global tl_name atkinson
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for the Atkinson Hyperlegible family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/atkinson
License:	lppl other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atkinson.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atkinson.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Atkinson Hyperlegible family of fonts, named after Braille Institute
founder, J. Robert Atkinson. What makes it different from traditional
typography design is that it focuses on letterform distinction to
increase character recognition, ultimately improving readability.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from atkinson:
Map atkinson.map
TL_DROPIN_EOF
