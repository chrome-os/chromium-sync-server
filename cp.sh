	
mkdir -p ~/workdir/sync-server
cd ~/workdir/sync-server

# Import require packages and fix imports for a standalone run
mkdir sync lib 
cp -rp ~/workdir/chromium/src/out/Default/pyproto/components/sync/protocol/ lib/protocol/ 
cp -rp ~/workdir/chromium/src/out/Default/pyproto/google .
cp -rp ~/workdir/chromium/src/components/sync/tools/testserver/ sync/testserver/ 
cp -rp ~/workdir/chromium/src/net/tools/testserver/ lib/testserver/ 
cp -rp ~/workdir/chromium/src/third_party/tlslite/tlslite/ . 

touch lib/testserver/__init__.py && \
touch lib/protocol/__init__.py && \
touch sync/testserver/__init__.py && \
touch sync/__init__.py && \
touch lib/__init__.py && \
sed -i 's#import echo_message#from lib.testserver import echo_message#' sync/testserver/sync_testserver.py && \
sed -i 's#import testserver_base#from lib.testserver import testserver_base#' sync/testserver/sync_testserver.py && \
/bin/bash -c 'for line in $(find ~/workdir/sync-server/lib/protocol/ -name "*.py" -type f -exec basename {} .py \;); do sed -i "s/import $line/from lib.protocol import $line/" ~/workdir/sync-server/sync/testserver/chromiumsync.py; done'
