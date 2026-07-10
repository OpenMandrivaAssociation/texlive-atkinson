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
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Atkinson Hyperlegible family of fonts, named after Braille Institute
founder, J. Robert Atkinson. What makes it different from traditional
typography design is that it focuses on letterform distinction to
increase character recognition, ultimately improving readability.

