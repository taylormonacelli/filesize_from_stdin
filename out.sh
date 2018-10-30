function moveup(){
    original_branch=`git rev-parse --abbrev-ref HEAD`
    sha1=$1
    if ! git cat-file -t $sha1 &>/dev/null; then
        echo cant find $sha1
        return
    fi
    rm -f 000*.patch
    export patch=0001*
    git format-patch --quiet -1 $sha1
    git config advice.detachedHead false
    git checkout --quiet ${sha1}~2
    govoner=0
    max_iter=500
    while git apply --check $patch 2>/dev/null && [[ $govoner -lt $max_iter ]]
    do
        h=$(git rev-parse --short HEAD)
        git checkout --quiet @~1
        (( govoner++ ))
    done




    [[ $govoner -eq $max_iter ]] && echo "warning: max iterations reached"
    git checkout --quiet $h
    git am --quiet --ignore-space-change --whitespace=nowarn $patch
    #	    if git rebase --preserve-merges --quiet HEAD $original_branch; then
    #			rm $patch
    #	    fi
}
