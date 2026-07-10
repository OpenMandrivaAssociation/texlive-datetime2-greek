%global tl_name datetime2-greek
%global tl_revision 47533

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Greek language module for the datetime2 package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-contrib/datetime2-greek
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-greek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-greek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-greek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This module provides the "greek" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is currently
unmaintained. Please see the README for the procedure to follow if you
want to take over the maintenance.

