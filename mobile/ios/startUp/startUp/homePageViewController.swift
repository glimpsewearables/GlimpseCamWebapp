//
//  homePageViewController.swift
//  startUp
//
//  Created by Alexis Macaskill on 9/24/18.
//  Copyright © 2018 Alexis Macaskill. All rights reserved.
//

import UIKit

struct EventDescriptionPractice {
    
    var id : Int
    var name : String
    var location : String
    var image : String
    
}

class homePageViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    @IBOutlet weak var tableView: UITableView!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    var events = [
        EventDescription(id: 1, name: "Lollapalooza", location: "Grant Park", image: "lolla"),
        EventDescription(id: 2, name: "Bumpershoot", location: "Seattle Center", image: "bumpershoot"),
        EventDescription(id: 3, name: "Coachella", location: "Indio", image: "coachella"),
        ]
    
    // MARK: - Table view data source
    
    // by default the tables have 1 section. This method isn't used right now
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return events.count
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return "Section \(section)"
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "LabelCell", for: indexPath)
        
        // cell.textLabel?.text = events[indexPath.row].name
        
        let event = events[indexPath.row]
        cell.textLabel?.text = event.name
        cell.detailTextLabel?.text = event.location
        cell.imageView?.image = UIImage(named: event.image)
        
        return cell
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
