pipenv run python server.py &
#retval=$?
#if [ $retval -ne 0 ]; then
    cd ../wordsmate_view && npm run postinstall && npm start &
#fi
