using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class interaction : MonoBehaviour
{
    public GameObject inputField;
    public string message;

    public GameObject medicalworker;

    private Animator animmodel;

    public void storename()
    {
        AudioSource[] audios = GetComponents<AudioSource>();


        animmodel = medicalworker.GetComponent<Animator>();


        animmodel.SetTrigger("back");

        message = inputField.GetComponent<Text>().text;
        if (message != null)
        {
            if (message == "Who are you" || message == "What is your name")
            {
                audios[0].Play();
                animmodel.SetTrigger("speak");




            }


            if (message == "I have fever" || message == "I got fever what to do")
            {
                audios[1].Play();
                animmodel.SetTrigger("speak");




            }


            if (message == "I have headache" || message == "My head is paining what to do")
            {
                audios[2].Play();
                animmodel.SetTrigger("speak");




            }


            if (message == "I have stomochache" || message == "My stomoch is aching")
            {
                audios[3].Play();
                animmodel.SetTrigger("speak");




            }

            if (message == "What problem can arise after covid19")
            {
                audios[4].Play();
                animmodel.SetTrigger("speak");




            }

            if (message == "Mental problem means what" || message == "What happens in mental problem")
            {
                audios[5].Play();
                animmodel.SetTrigger("speak");




            }

            if (message == "What is anxiety")
            {
                audios[6].Play();
                animmodel.SetTrigger("speak");




            }

            if (message == "How to avoid mental problems" || message == "How to cure mental illness")
            {
                audios[7].Play();
                animmodel.SetTrigger("speak");




            }

            if (message == "How to keep mind balanced" || message == "How to make mind calm")
            {
                audios[8].Play();
                animmodel.SetTrigger("speak");




            }

            StartCoroutine(ExampleCoroutine());
        }
        
    }
    IEnumerator ExampleCoroutine()
    {
        

        //yield on a new YieldInstruction that waits for 7 seconds.
        yield return new WaitForSeconds(7);

       
    }
}