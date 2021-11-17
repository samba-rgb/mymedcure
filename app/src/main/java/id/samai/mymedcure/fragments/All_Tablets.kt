package id.samai.mymedcure.fragments

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.Toast
import android.widget.Toast.makeText
import androidx.recyclerview.widget.LinearLayoutManager
import id.samai.mymedcure.R
import id.samai.mymedcure.adapters.all_medicine_Adapter
import id.samai.mymedcure.adapters.morningAdapter
import id.samai.mymedcure.extensions.dbHelper
import id.samai.mymedcure.helpers.Formatter
import kotlinx.android.synthetic.main.fragment_all__tablets.view.*


import kotlinx.android.synthetic.main.fragment_schedule.view.schedule_empty_layout
import kotlinx.android.synthetic.main.fragment_schedule.view.schedule_recycler_view_list
// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER

/**
 * A simple [Fragment] subclass.
 * Use the [All_Tablets.newInstance] factory method to
 * create an instance of this fragment.
 */
class All_Tablets :Fragment() {
    lateinit var view: ViewGroup
    lateinit var diceImage : ImageView

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        view = (inflater.inflate(R.layout.fragment_all__tablets, container, false) as ViewGroup).apply {



            initRecylerView(this)



        }

        return view
    }

    override fun onResume() {
        initRecylerView(view)

        super.onResume()
    }


    private fun initRecylerView(view: View) {
        view.apply {
            val day = Formatter.getdayforfragment()

            val schedules = context.dbHelper.getallmedicine(day)


            if (schedules.isEmpty()) {
                Toast.makeText(context, "empty", Toast.LENGTH_SHORT).show()
                schedule_recycler_view_list.visibility = View.GONE
                schedule_empty_layout.visibility = View.VISIBLE
            } else {
                schedule_recycler_view_list.visibility = View.VISIBLE
                schedule_empty_layout.visibility = View.GONE

                val scheduleAdapter = all_medicine_Adapter(context, schedules)
                schedule_recycler_view_list.apply {
                    layoutManager = LinearLayoutManager(context)
                    adapter = scheduleAdapter
                }
            }
        }
    }

}