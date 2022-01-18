# generate_pdf_in_cloud_functions_to_cloud_storage

## requirements

### setup Cloud SDK

https://cloud.google.com/sdk/docs/quickstart

### setup Cloud Storage

https://sleepless-se.net/2018/05/22/googlecloudstorage%E3%81%A7python%E3%81%8B%E3%82%89%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E3%82%84%E3%82%8A%E3%81%A8%E3%82%8A%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/#PythonCloudStorage

## install dependencies

```
pip install -r requirements.txt
```

## develop in local

```
functions-framework --target sample --signature-type=http --port=8080 --debug
```

## deploy
```
gcloud functions deploy sample --runtime python39 --trigger-http --allow-unauthenticated
```
