#! /bin/bash


docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py \
        -t http://testhtml5.vulnweb.com -g gen.conf -J test_report.json
sleep 1

# FILE = "test_report.json"

if [ -e "test_report.json" ]
then
    python JSON_parser.py
fi


