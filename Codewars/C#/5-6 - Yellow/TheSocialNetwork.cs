// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/5884a4642a8d88df67000026
// # Notes  : tag-codewars, tag-kyu-5
// #-----------------------------------------------------------

using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Codewars
{
    public class SocialNetwork : ISocialNetwork
    {
        private List<IMember> members = new List<IMember>();
        // Total number of members currently in the social network
        public int MemberCount { get { return members.Count; } }

        // Adds a new member and returns the added member
        public IMember AddMember(string firstName, string lastName, string city, string country)
        {
            var member = new Member(firstName, lastName, city, country);
            members.Add(member);
            return member;
        }

        // Returns the member with the id
        public IMember FindMemberById(int id) =>
            members.FirstOrDefault(memb => memb.Id == id);

        // Returns a list of members by searching all fields in the profile
        public IEnumerable<IMember> FindMember(string search)
        {
            var memb = new List<IMember>();
            foreach (var person in members)
            {
                if (person.Profile.Firstname.Equals(search) || person.Profile.Lastname.Equals(search))
                    memb.Add(person);
            }

            return memb;
        }
    }

    public class Member : IMember
    {
        public IList<IMember> _friends = new List<IMember>();
        public IList<IMember> _pending = new List<IMember>();
        public IList<IPost> _posts = new List<IPost>();


        // Id of member. Must be unique and sequential. 
        public int Id { get; }
        // Member profile
        public IMemberProfile Profile { get; }
        // List of friends
        public IEnumerable<IMember> Friends { get { return _friends; } }
        // List of pending friend requests
        public IEnumerable<IMember> Pending { get { return _pending; } }
        // Members posts
        public IEnumerable<IPost> Posts { get { return _posts; } }

        internal Member(string firstName, string lastName, string city, string country)
        {
            Id = IdGenerator.GetId<IMember>();
            Profile = new MemberProfile(Id, firstName, lastName, city, country);
        }

        // Adds a friend request for this member. from - the member making the friend request 
        public void AddFriendRequest(IMember from)
        {
            if (from.Id == Id)
                return;

            if (_pending.FirstOrDefault(memb => memb.Id == from.Id) == null &
                _friends.FirstOrDefault(memb => memb.Id == from.Id) == null)
            {
                _pending.Add(from);
                (from as Member)._pending.Add(this);
            }
        }

        // Confirms a pending friend request
        public void ConfirmFriend(IMember member)
        {
            var approve = _pending.FirstOrDefault(memb => memb.Id == member.Id);
            if (approve != null & _friends.FirstOrDefault(memb => memb.Id == member.Id) == null)
            {
                _pending.Remove(approve);
                _friends.Add(approve);

                (member as Member)._friends.Add(this);
                (member as Member)._pending.Remove(this);
            }
        }



        // Removes a pending friend request
        public void RemoveFriendRequest(IMember member)
        {
            _pending.Remove(member);
            (member as Member)._pending.Remove(this);
        }

        // Removes a friend
        public void RemoveFriend(IMember member)
        {
            _friends.Remove(member);
            (member as Member)._friends.Remove(this);
        }

        // Returns a list of all friends. level - depth (1 - friends, 2 - friends of friends ...)
        public IEnumerable<IMember> GetFriends(int level = 1, IList<int> filter = null)
        {
            var allFriends = new List<IMember>();
            allFriends.AddRange(_friends);

            if (level > 1)
            {
                foreach (var friend in _friends)
                    allFriends.AddRange(friend.GetFriends(level - 1, filter));

                allFriends = allFriends.GroupBy(p => p.Id).Select(g => g.First()).Where(x => x.Id != this.Id).ToList();
            }

            return allFriends;
        }

        // Adds a new post to members feed
        public IPost AddPost(string message)
        {
            var post = new Post(IdGenerator.GetId<IPost>(), this, message);
            _posts.Add(post);
            return post;
        }

        // Removes the post with the id
        public void RemovePost(int id) => _posts.Remove(_posts.FirstOrDefault(p => p.Id == id));

        // Returns members feed as a list of posts. Should also return posts of friends.
        public IEnumerable<IPost> GetFeed()
        {
            var allFeed = new List<IPost>();
            allFeed.AddRange(_posts);
            foreach (var friends in _friends)
                allFeed.AddRange(friends.Posts);


            var aaaa = allFeed.OrderBy(memb => memb.Id).ToList();
            foreach (var __feed in aaaa)
                Console.WriteLine(__feed.Id);

            return allFeed.OrderBy(x => x.Id);
        }
    }

    public class MemberProfile : IMemberProfile
    {
        // Id of the Member this profile belongs to
        public int MemberId { get; set; }

        public string Firstname { get; set; }
        public string Lastname { get; set; }
        public string City { get; set; }
        public string Country { get; set; }

        public MemberProfile(int memberId, string firstName, string lastName, string city, string country)
        {
            MemberId = memberId;
            Firstname = firstName;
            Lastname = lastName;
            City = city;
            Country = country;
        }
    }

    public class Post : IPost
    {
        // Id of post. Must be unique and sequential.
        public int Id { get; set; }
        // Member that made this post
        public IMember Member { get; set; }
        // The post message
        public string Message { get; set; }
        // Date and time post was made
        public DateTime Date { get; set; }
        // Likes for post
        public int Likes { get; set; }

        public Post(int id, IMember member, string message)
        {
            Id = id;
            Member = member;
            Message = message;
            Date = DateTime.Now;
            Likes = 0;
        }
    }
}