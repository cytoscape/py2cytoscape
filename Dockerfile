# Copyright (c) Bioinformatics Core Facility of the Max Planck Institute for Biology of Ageing.
# Distributed under the terms of the Modified BSD License.

# Debian buster-slim (10.1) image available on 20 Wednesday 2020.
FROM debian@sha256:11253793361a12861562d1d7b15b8b7e25ac30dd631e3d206ed1ca969bf97b7d

LABEL maintainer "bioinformatics@age.mpg.de"

USER root

ENV DEBIAN_FRONTEND noninteractive

ENV MODS /modules
ENV SOFT $MODS/software
ENV SOUR $MODS/sources/
ENV MODF $MODS/modulefiles
ENV LOGS $MODS/installation_logs

RUN mkdir -p $SOFT $SOUR $MODF $LOGS $MODF/bioinformatics $MODF/general $MODF/libs

RUN echo "deb http://ftp.debian.org/debian buster main non-free contrib" >> /etc/apt/sources.list && \
echo "deb-src http://ftp.debian.org/debian buster main non-free contrib" >> /etc/apt/sources.list && \
echo "deb http://ftp.debian.org/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
echo "deb-src http://ftp.debian.org/debian buster-updates main contrib non-free" >> /etc/apt/sources.list

RUN REPO=http://cdn-fastly.deb.debian.org && \
echo "deb $REPO/debian buster main\ndeb $REPO/debian-security buster/updates main" > /etc/apt/sources.list && \
apt-get update && apt-get -yq dist-upgrade && \
apt-get install -yq --no-install-recommends locales && \
apt-get clean && rm -rf /var/lib/apt/lists/* && \
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

RUN apt-get update && \
apt-get install -yq --no-install-recommends \ 
   libreadline-dev \
   xorg-dev \
   apt-utils \
   wget \
   bzip2 \
   ca-certificates \
   sudo \
   jed \
   emacs \
   build-essential \
   python-dev \
   unzip \
   libsm6 \
   pkg-config \
   pigz \
   zlib1g-dev \
   autoconf \
   automake \
   environment-modules \
   gcc && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
apt-get install -yq --no-install-recommends \
   f2c \   
   git \
   vim \
   texlive-latex-base \
   texlive-latex-extra \
   texlive-fonts-extra \
   texlive-fonts-recommended \
   pandoc \
   texlive-generic-recommended \
   libxrender1 \
   inkscape \
   libxml2-dev \
   libcurl4-gnutls-dev \
   libatlas3-base \
   libopenblas-base \
   libfreetype6-dev \
   libtool \
   libexpat1-dev \
   libxml2-dev \
   libxslt1-dev && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
apt-get install -yq --no-install-recommends \ 
   ghostscript \
   gfortran \
   libpcre3 \
   libpcre3-dev \
   libssl-dev \
   libsqlite3-dev \
   libssl-dev \
   libfreetype6-dev \
   libpng-dev \
   liblmdb-dev \
   libmariadb-dev \
   libmariadb-client-lgpl-dev-compat \
   libtbb2 \
   libtbb-dev \
   curl \
   libcurl4 \
   libcurl4-openssl-dev \
   libncurses5-dev \
   libcairo2-dev \
   libtool-bin \
   libzmq3-dev \
   zip && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
apt-get install -yq --no-install-recommends \ 
   tk \
   tcl \
   openssl \
   libssl-dev \
   libssh2-1-dev \
   libtool \
   libffi-dev \
   ruby \
   ruby-dev \
   make \
   libzmq3-dev \
   libczmq-dev \
   apt-transport-https \
   dirmngr \
   cmake \
   libpam0g-dev \
   lsb-release \
   libedit2 \
   libapparmor1 \
   gnupg \
   liblzma-dev \
   psmisc \
   less \
   libclang-dev && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

RUN cd ${SOUR} && \
    wget http://ftp.de.debian.org/debian/pool/main/o/openssl/libssl1.1_1.1.1d-0+deb10u2_amd64.deb && \
    dpkg -i libssl1.1_1.1.1d-0+deb10u2_amd64.deb && \
    rm -rf ${SOUR}/*


RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/debian stable-buster main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt update && apt-get -y install mono-devel && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV SHELL /bin/bash
ENV NB_USER mpiage
ENV NB_UID 1000
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER ; \
echo "root:bioinf" | chpasswd ; \
echo "mpiage:bioinf" | chpasswd ; \
adduser mpiage sudo

# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
    echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

RUN wget https://raw.githubusercontent.com/mpg-age-bioinformatics/draco_pipelines/master/software/newmod.sh \
&& sed -i 's/u\/jboucas\/modules/modules/g' newmod.sh && chmod 777 newmod.sh && mv newmod.sh /usr/bin

ENV MODULEPATH $MODF/bioinformatics:$MODF/general:$MODF/libs

# gsl
RUN cd $SOUR && wget ftp://ftp.gnu.org/gnu/gsl//gsl-2.6.tar.gz && \
  mkdir -p $SOFT/gsl/2.6.0 && \
  tar -zxvf gsl-2.6.tar.gz && \
  cd gsl-2.6 && \
  ./configure --prefix=$SOFT/gsl/2.6.0 && \
  make && \
  make install && \
  newmod.sh \
  -s gsl \
  -p $MODF/libs/ \
  -v 2.6.0 \
  -d 2.6.0 && \
  echo "prepend-path LIBRARY_PATH /modules/software/gsl/2.6.0/lib" >> $MODF/libs/gsl/2.6.0 && \
  rm -rf $SOUR/*

# bzip2
RUN cd $SOUR && wget https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz && \
    tar -xzf bzip2-1.0.8.tar.gz && \
    cd bzip2-1.0.8 && \
    mkdir -p $SOFT/bzip2/1.0.8 && \
    sed -i "18s/.*/CC\=gcc -fPIC/" Makefile && \
    make -f Makefile-libbz2_so COMPILE_FLAGS+=-fPIC && make clean && make COMPILE_FLAGS+=-fPIC && \
    make -n install PREFIX=$SOFT/bzip2/1.0.8 COMPILE_FLAGS+=-fPIC && make install PREFIX=$SOFT/bzip2/1.0.8 COMPILE_FLAGS+=-fPIC && \
    cp -v bzip2-shared $SOFT/bzip2/1.0.8/bin/bzip2 && \
    cp -av libbz2.so* $SOFT/bzip2/1.0.8/lib && \
    newmod.sh \
    -s bzip2 \
    -p $MODF/libs/ \
    -v 1.0.8 \
    -d 1.0.8 && \
    rm -rf $SOUR/*

# xz
RUN cd $SOUR && wget http://tukaani.org/xz/xz-5.2.4.tar.gz && \
    tar -xzf xz-5.2.4.tar.gz && \
    cd xz-5.2.4 && \
    mkdir -p $SOFT/xz/5.2.4 && \
    ./configure --prefix=$SOFT/xz/5.2.4 && make && make install && \
    newmod.sh \
    -s xz \
    -p $MODF/libs/ \
    -v 5.2.4 \
    -d 5.2.4 && \
    rm -rf $SOUR/*

# openblas
RUN cd $SOUR && wget https://github.com/xianyi/OpenBLAS/archive/v0.3.7.tar.gz && \
    mv v0.3.7.tar.gz openblas-0.3.7.tar.gz && \
    tar -xzf openblas-0.3.7.tar.gz && \
    cd OpenBLAS-0.3.7 && \
    mkdir -p $SOFT/openblas/0.3.7 && \
    make PREFIX=$SOFT/openblas/0.3.7 && \
    make install PREFIX=$SOFT/openblas/0.3.7 && \
    newmod.sh \
    -s openblas \
    -p $MODF/libs/ \
    -v 0.3.7 \
    -d 0.3.7 && \
    rm -rf $SOUR/*

# jre
RUN cd $SOUR && wget -O jre-8.0.231-linux-x64.tar.gz https://javadl.oracle.com/webapps/download/AutoDL?BundleId=240718_5b13a193868b4bf28bcb45c792fce896 && \
    tar -zxvf jre-8.0.231-linux-x64.tar.gz && \
    cd jre1.8.0_231 && \
    mkdir -p $SOFT/jre/8.0.231&& \
    cp -r * $SOFT/jre/8.0.231/ && \
    newmod.sh \
    -s jre \
    -p $MODF/general/ \
    -v 8.0.231 \
    -d 8.0.231 && \
    echo "setenv JAVA_HOME $SOFT/jre/8.0.231" >> $MODF/general/jre/8.0.231 && \
    rm -rf $SOUR/*

# jdk
RUN cd $SOUR && \
    wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/13.0.1+9/cec27d702aa74d5a8630c65ae61e4305/jdk-13.0.1_linux-x64_bin.tar.gz && \
    tar -xvzf jdk-13.0.1_linux-x64_bin.tar.gz && \
    mkdir -p $SOFT/jdk/13.0.1/bin && \
    cd jdk-13.0.1 && \
    cp -r * $SOFT/jdk/13.0.1/ && \
    newmod.sh \
    -s jdk \
    -p $MODF/general/ \
    -v 13.0.1 \
    -d 13.0.1 && \
    echo "setenv JAVA_HOME $SOFT/jdk/13.0.1" >> $MODF/general/jdk/13.0.1 && \
    rm -rf $SOUR/*

# perl/cpanm
RUN mkdir -p $SOFT/perl/5.28.1/bin && \
    cd $SOFT/perl/5.28.1/bin && \
    curl -L https://cpanmin.us/ -o cpanm && \
    chmod +x cpanm && \
    newmod.sh -s perl -p $MODF/general -v 5.28.1 -d 5.28.1 && \
    echo 'set home $::env(HOME)' >> $MODF/general/perl/5.28.1 && \
    echo 'set perluser $home/.software_container/.perl/5.28.1' >> $MODF/general/perl/5.28.1 && \
    echo 'exec /bin/mkdir -p $perluser' >> $MODF/general/perl/5.28.1 && \
    echo 'prepend-path PERL5LIB $perluser/lib/perl5' >> $MODF/general/perl/5.28.1 && \
    echo 'setenv PERLUSER $perluser' >> $MODF/general/perl/5.28.1

# Install R-3.6.1
RUN /bin/bash -c 'source /etc/profile.d/modules.sh && \
    module load bzip2/1.0.8 && \
    module load xz/5.2.4 && \
    module load jdk/13.0.1 && \
    cd $SOUR && wget http://ftp5.gwdg.de/pub/misc/cran/src/base/R-3/R-3.6.1.tar.gz && \
    tar -xzf R-3.6.1.tar.gz && \
    cd R-3.6.1 && \
    mkdir -p $SOFT/rlang/3.6.1/bin && \
    ./configure --prefix=$SOFT/rlang/3.6.1 \
    CFLAGS="-I$SOFT/bzip2/1.0.8/include \
    -I$SOFT/xz/5.2.4/include \
    -I$SOFT/jdk/13.0.1/include" \
    LDFLAGS="-L$SOFT/bzip2/1.0.8/lib \
    -L$SOFT/xz/5.2.4/lib \
    -L$SOFT/jdk/13.0.1/lib" \
    --with-cairo=yes --with-libpng=yes \
    --with-readline --with-tcltk --enable-R-profiling \
    --enable-R-shlib=yes --enable-memory-profiling --with-blas --with-lapack && \
    make && make install && \
    newmod.sh \
    -s rlang \
    -p $MODF/general/ \
    -v 3.6.1 \
    -d 3.6.1 && \
    echo "set home $::env(HOME)" >> $MODF/general/rlang/3.6.1 && \
    echo "exec /bin/mkdir -p \$home/.software_container/.R/3.6.1/R_LIBS_USER/" >> $MODF/general/rlang/3.6.1 && \
    echo "setenv R_LIBS_USER \$home/.software_container/.R/3.6.1/R_LIBS_USER" >> $MODF/general/rlang/3.6.1 && \
    echo "prepend-path LD_LIBRARY_PATH $SOFT/rlang/3.6.1/lib/R/lib" >> $MODF/general/rlang/3.6.1 && \
    echo "prepend-path CPATH $SOFT/rlang/3.6.1/lib/R/include" >> $MODF/general/rlang/3.6.1 && \
    echo "prepend-path C_INCLUDE_PATH $SOFT/rlang/3.6.1/lib/R/include" >> $MODF/general/rlang/3.6.1 && \
    echo "prepend-path CPLUS_INCLUDE_PATH $SOFT/rlang/3.6.1/lib/R/include" >> $MODF/general/rlang/3.6.1 && \
    echo "prepend-path OBJC_INCLUDE_PATH $SOFT/rlang/3.6.1/lib/R/include" >> $MODF/general/rlang/3.6.1 && \
    echo "module load jdk/13.0.1" >> $MODF/general/rlang/3.6.1 && \
    echo "setenv CFLAGS \"-I$SOFT/jdk/13.0.1/include -I$SOFT/bzip2/1.0.8/include -I$SOFT/xz/5.2.4/include\"" >> $MODF/general/rlang/3.6.1 && \
    echo "setenv LDFLAGS \"-L$SOFT/jdk/13.0.1/lib -L$SOFT/bzip2/1.0.8/lib -L$SOFT/xz/5.2.4/lib\"" >> $MODF/general/rlang/3.6.1' && \
    rm -rf ${SOUR}/*

# jupyterhub v2.0.0
RUN cd $SOUR && \
    wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz && \
    wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz && \
    tar xzf Python-3.8.0.tgz && \
    tar xzf Python-2.7.16.tgz && \
    /bin/bash -c 'source /etc/profile.d/modules.sh && \
    module load openblas/0.3.7 && \
    cd $SOUR/Python-2.7.16 && \
    mkdir -p $SOFT/jupyterhub/1.0.0/bin && \
    ./configure --prefix=$SOFT/jupyterhub/1.0.0 --enable-loadable-sqlite-extensions --enable-shared --with-ensurepip=yes \
      CLFAGS="-I$SOFT/openblas/0.3.7/include" \
      LDFLAGS="-L$SOFT/openblas/0.3.7/lib" && \
    make && make install && \
    cd $SOUR/Python-3.8.0 && \
    ./configure --prefix=$SOFT/jupyterhub/1.0.0 --enable-loadable-sqlite-extensions --enable-shared -with-ensurepip=yes \
    CLFAGS="-I$SOFT/openblas/0.3.7/include" \
    LDFLAGS="-L$SOFT/openblas/0.3.7/lib" && \
    make && make install && \
    newmod.sh \
    -s jupyterhub \
    -p $MODF/general/ \
    -v 1.0.0 \
    -d 1.0.0 && \
    echo "set home $::env(HOME)" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "set pythonuser \$home/.software_container/.jupyterhub/1.0.0/bin" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "exec /bin/mkdir -p \$pythonuser" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "prepend-path PATH \$home/.software_container/.jupyterhub/1.0.0/bin" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "set jupyter_runtime_dir \$home/.software_container/.jupyterhub/1.0.0/jupyter/run" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "exec /bin/mkdir -p \$jupyter_runtime_dir" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "setenv JUPYTER_RUNTIME_DIR \$home/.software_container/.jupyterhub/1.0.0/jupyter/run" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "set jupyter_data_dir \$home/.software_container/.jupyterhub/1.0.0/jupyter/data" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "exec /bin/mkdir -p \$jupyter_data_dir" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "setenv JUPYTER_DATA_DIR \$home/.software_container/.jupyterhub/1.0.0/jupyter/data" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "setenv PYTHONHOME $SOFT/jupyterhub/1.0.0/" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "setenv PYTHONUSERBASE \$home/.software_container/.jupyterhub/1.0.0/" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "exec /bin/mkdir -p \$home/.software_container/.jupyterhub/1.0.0/pythonpath/site-packages" >> $MODF/general/jupyterhub/1.0.0 && \
    echo "module load openblas/0.3.7 rlang/3.6.1" >> $MODF/general/jupyterhub/1.0.0 && \
    module load jupyterhub/1.0.0 && \
    pip3 install jupyter && \
    python2 -m pip install ipykernel && \
    python2 -m ipykernel install' && \
    rm -rf ${SOUR}/*

## Libraries required for jupyter R kernel
RUN echo "install.packages('askpass', repos='http://cran.us.r-project.org')" > $SOUR/askpass.install.R && \
    echo "install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'), lib=c('$SOFT/rlang/3.6.1/lib/R/library')  ,repos=c('http://ftp5.gwdg.de/pub/misc/cran/'), dependencies=TRUE )" > $SOUR/jupyter.install.R && \
    echo "devtools::install_github('IRkernel/IRkernel',lib=c('$SOFT/rlang/3.6.1/lib/R/library')) " >> $SOUR/_jupyter.install.R && \
    echo "IRkernel::installspec(name = 'ir361', displayname = 'R 3.6.1')" > $SOUR/.install.jupyter.R.kernel.3.6.1

RUN /bin/bash -c 'source /etc/profile.d/modules.sh && \
    module load jupyterhub && \
    module load rlang && \
    cd $SOUR && \
    $SOFT/rlang/3.6.1/bin/Rscript $SOUR/askpass.install.R && \
    wget -O openssl_1.3.0.tar.gz https://github.com/jeroenooms/openssl/archive/v1.3.0.tar.gz && \
    $SOFT/rlang/3.6.1/bin/R CMD INSTALL -l $SOFT/rlang/3.6.1/lib/R/library openssl_1.3.0.tar.gz && \
    git clone https://github.com/ropensci/git2r.git && \
    $SOFT/rlang/3.6.1/bin/R CMD INSTALL -l $SOFT/rlang/3.6.1/lib/R/library git2r && \
    $SOFT/rlang/3.6.1/bin/Rscript $SOUR/jupyter.install.R && \
    $SOFT/rlang/3.6.1/bin/Rscript $SOUR/_jupyter.install.R && \
    Rscript $SOUR/.install.jupyter.R.kernel.3.6.1 && rm $SOUR/jupyter.install.R $SOUR/_jupyter.install.R $SOUR/.install.jupyter.R.kernel.3.6.1' && \
    rm -rf ${SOUR}/*
## Finished installation of jupyter R kernel

## Install rstudio server ##
RUN /bin/bash -c 'source /etc/profile.d/modules.sh && \
    module load jupyterhub && \
    module load rlang && \
    cd ${SOUR} && \
    wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.5019-amd64.deb && \
    dpkg -i rstudio-server-1.2.5019-amd64.deb && \
    echo "rsession-which-r=$(which R)" >> /etc/rstudio/rserver.conf' && \  
    rm -rf ${SOUR}/*

RUN /bin/bash -c 'source /etc/profile.d/modules.sh && \
  module load jre && \
  mkdir -p $SOFT/cytoscape/3.7.2 && \
  cd $SOFT/cytoscape/3.7.2 && wget  https://github.com/cytoscape/cytoscape/releases/download/3.7.2/Cytoscape_3_7_2_unix.sh && \
  bash Cytoscape_3_7_2_unix.sh -q && \
  newmod.sh \
  -s cytoscape \
  -p $MODF/bioinformatics/ \
  -v 3.7.2 \
  -d 3.7.2 && \
  echo "module load jre" >> $MODF/bioinformatics/cytoscape/3.7.2  && \
  echo "prepend-path PATH /usr/local/Cytoscape_v3.7.2" >> $MODF/bioinformatics/cytoscape/3.7.2' && \
  rm -rf ${SOUR}/*

USER $NB_USER

RUN mkdir /home/$NB_USER/py2cytoscape

# COPY * /home/$NB_USER/py2cytoscape

# RUN /bin/bash -c 'source /etc/profile.d/modules.sh && \
#     module load jupyterhub && \
#     cd py2cytoscape && \
#     python3 setup.py develop --user'

##########################
#### this part to end ####
##########################

# Jupyter port
EXPOSE 8888
# rstudio server port
EXPOSE 8787

COPY .bashrc /home/$NB_USER/.bashrc

RUN echo "options(bitmapType='cairo')" > /home/$NB_USER/.Rprofile
RUN mkdir -p /home/$NB_USER/.software_container/.jupyter
COPY jupyter_notebook_config.py /home/$NB_USER/.software_container/.jupyter/
USER root

# Folders in home folder that should be kept
ENV HOFOL ".bashrc .bash_logout .Rprofile .software_container"

RUN for i in $(ls /home/mpiage/) ; do echo ${i}; done

RUN mkdir -p /home/_mpiage \
&& for f in $HOFOL ; do \
  if [ ! -e /home/mpiage/${f} ] ;\
    then echo 'no ${f}..' ;\
  else cp -rv /home/mpiage/${f} /home/_mpiage/; \
  fi \ 
done

ENTRYPOINT /bin/bash -c '\
for f in $HOFOL ; do \
  if [[ ! -e /home/mpiage/${f} ]] ; \
    then cp -vr /home/_mpiage/${f} /home/mpiage/${f}; \
  fi \
done \
&& source /home/mpiage/.bashrc \
&& /bin/bash'
WORKDIR /home/mpiage
RUN chown -R mpiage: /home/mpiage

RUN mkdir -p /Dockerfiles/v3.0.0s
COPY Dockerfile /Dockerfiles/v3.0.0s/

USER $NB_USER

