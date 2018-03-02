Kubernetes setup and deployment in GCloud
=========================================


whith this setup you will be able to configure a Kubernetes cluster  in Googoe Cloud and install Go CD.

Prerequisites
--------------

You'll need this tools installed and configurated to acomplish this task

1. [Kubernetes => v.1.7.5](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
2. [Ansible  => v.0.10.8](http://docs.ansible.com/ansible/latest/intro_installation.html)
3. [Google Cloud SDK => 190.0.1](https://cloud.google.com/sdk/)
4. A [Google Cloud account](https://cloud.google.com/)
5. Python v2.7.X
6. Gomatic [Python Library](https://github.com/gocd-contrib/gomatic) 
7. Helm, the [Kubernetes Package Manager](https://github.com/kubernetes/helm#install) 
8. A project created on Google Cloud.
9. Change the project name used for your own project name en the `group_vars/all/all` file. Feel fre to change the other variables if you wish.
10. Create a `user.txt` file and a `password.txt` file in the ROOT folder to configure the access to the cluster. This user and password will be encrypted later by kubernetes.

    Example for `user.txt`
        
        user_admin

Steps to depoy this playbook
---------------------------

1. Connect to GC `gcloud init`
2. Configure your accout with the name of the project and region.
3. Execute the Ansible Playbook

  ```
    ansible-playbook -vvvv  cluster.yml 
  ```

4. Access to GoCD GIU and enable the agent
5. Create a new environment and attach the pipeline and the agent
6. Watch the execution 


# More Information?


* My [mail](mailto:andres.torresduran@gmail.com)
* My [GitLab account](https://gitlab.com/aetorres)
* My [Bitbucket account](https://bitbucket.org/aetorres/)
* My [GitLab account](https://github.com/aetorres)
* My [Twitter](https://twitter.com/Andr3s_T)
