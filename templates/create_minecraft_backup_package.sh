
cd {{ host.install_folder }}
echo "---"
echo "packaging minecraft folder..."
tar -cvjf ../minecraft.tar.bz2 .
echo "---"
ls -la {{ host.install_folder }}/../
echo "---"
ls -la {{ host.install_folder }}/../minecraft.tar.bz2
