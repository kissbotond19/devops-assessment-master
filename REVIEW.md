# Code Review

## top 5 most important things (regarding the already completed helm and terraform part)

- Make the chart more "templatable" -> control most of the variables via the Helm chart's values.yaml instead of statically hardcode them in the template yamls.

- Double-check and fix the misconfigurations, such as containerPort/targetPort and Service selector/Deployment label/Ingress backend name discrepancies.

- Use variables instead of hardcode, where it's applicable.

- Add some output values which may be useful in the future.

- In case of further assistance would be needed regarding the image build or the CI pipeline part, call me on Teams/Zoom.;)

