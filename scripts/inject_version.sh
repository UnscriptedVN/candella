#!/bin/bash

# You find yourself in a strange place. This is where we inject semvering via Git Tags
# No need to change anything below the replacer variable.
# Just change the value of replacer, the script will do everything for you

replacer="2.0.0"
shortened_hash="$(echo $commit | head -c 7)"

if [[ $tag == "refs/tags/"* ]]; then
    tag_remove="refs/tags/"
    new_tag=${tag#"${tag_remove}"}
    tag=$new_tag
fi

if [ ! -z $tag ]; then
  echo "Tag ${tag} found. Using tag..."
  sed -i "s/define config.version = \"$replacer\"/define config.version = \"${tag}-rpy_${sdk}\"/g" game/options.rpy;
  sed -i "s/\"BUILD_ID\": \"GITHASH\"/\"BUILD_ID\":  \"$tag\"/g" game/System/ASDefinitions.rpy;
  cat game/options.rpy | grep config.version;
  cat game/System/ASDefinitions.rpy | grep BUILD_ID;
else
  echo "No tag found. Using Git hash..."
  sed -i "s/config.version = \"$replacer\"/config.version = \"${shortened_hash}-rpy_${sdk}\"/g" game/options.rpy;
  sed -i "s/\"BUILD_ID\": \"GITHASH\"/\"BUILD_ID\":  \"$shortened_hash\"/g" game/System/ASDefinitions.rpy;
  cat game/options.rpy | grep config.version;
  cat game/System/ASDefinitions.rpy | grep BUILD_ID;
fi
