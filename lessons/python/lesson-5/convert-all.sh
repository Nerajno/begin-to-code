for f in *.tif; do
  echo "Converting $f";
  convert "$f"  "$(basename "$f" .tif).jpg";
  rm $f;
done
