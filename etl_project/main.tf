terraform {
  required_providers {
    null = {
      source = "hashicorp/null"
      version = "3.1.1"
    }
  }
}

resource "null_resource" "download_csv" {
  provisioner "local-exec" {
    command = "python download.py"
  }

  triggers = {
    always_run = "${timestamp()}"
  }
}

resource "null_resource" "run_etl" {
  provisioner "local-exec" {
    command = "python etl.py"
  }

  depends_on = [null_resource.download_csv]

  triggers = {
    always_run = "${timestamp()}"
  }
}

resource "null_resource" "launch_streamlit" {
  provisioner "local-exec" {
    command = "nohup streamlit run app.py &"
    working_dir = "${path.module}"
  }

  triggers = {
    always_run = "${timestamp()}" # force à relancer à chaque `terraform apply`
  }
}
