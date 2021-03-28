using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class PlacementIndicator : MonoBehaviour
{
    private ARRaycastManager rayManager;
    private GameObject visual;
    public GameObject objectToSpawn;
    private GameObject obj;

    void Start ()
    {
        // get the components
        rayManager = FindObjectOfType<ARRaycastManager>();
        visual = transform.GetChild(0).gameObject;

        // hide the placement visual
        visual.SetActive(false);
    }

    void Update ()
    {
        if(obj == null)
        {
            // shoot a raycast from the center of the screen
            List<ARRaycastHit> hits = new List<ARRaycastHit>();
            rayManager.Raycast(new Vector2(Screen.width / 2, Screen.height / 2), hits, TrackableType.Planes);

            // if we hit an AR plane, update the position and rotation
            if (hits.Count > 0)
            {
                transform.position = hits[0].pose.position;
                transform.rotation = hits[0].pose.rotation;

                if (!visual.activeInHierarchy)
                    visual.SetActive(true);
            }

            if (Input.touchCount > 0 && Input.touches[0].phase == TouchPhase.Began)
            {
                obj = Instantiate(objectToSpawn,
                transform.position, transform.rotation);

            }
        }

        if(obj != null)
        {
            visual.SetActive(false);
        }
        

    }
}